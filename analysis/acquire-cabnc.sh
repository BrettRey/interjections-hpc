#!/usr/bin/env bash
set -euo pipefail

repo_url="https://github.com/saulalbert/CABNC.git"
commit_sha="0a28a11e168e312d1b9ad406a3352f31c13b86a2"
subtree_path="data/cabnc_talkbank_chat"
subtree_sha="7f7f87611350439e404baa8f8c659f33e81efecb"

project_root="$(cd "$(dirname "$0")/.." && pwd)"
target_dir="$project_root/vendor/CABNC-0a28a11"

if [[ -e "$target_dir" ]]; then
  if [[ ! -d "$target_dir/.git" ]]; then
    echo "Refusing to use existing non-git path: $target_dir" >&2
    exit 1
  fi
  observed_commit="$(git -C "$target_dir" rev-parse HEAD)"
  observed_subtree="$(git -C "$target_dir" rev-parse "HEAD:$subtree_path")"
  if [[ "$observed_commit" != "$commit_sha" || "$observed_subtree" != "$subtree_sha" ]]; then
    echo "Existing CABNC checkout does not match the frozen source." >&2
    exit 1
  fi
  if [[ -n "$(git -C "$target_dir" status --porcelain --untracked-files=all)" ]]; then
    echo "Existing CABNC checkout is dirty; refusing to use it." >&2
    exit 1
  fi
  echo "$target_dir"
  exit 0
fi

mkdir -p "$project_root/vendor"
mkdir "$target_dir"
git -C "$target_dir" init
git -C "$target_dir" remote add origin "$repo_url"
git -C "$target_dir" sparse-checkout init --no-cone
git -C "$target_dir" sparse-checkout set /README.md "/$subtree_path/"
git -C "$target_dir" fetch --filter=blob:none --depth 1 origin "$commit_sha"
git -C "$target_dir" checkout --detach FETCH_HEAD

observed_commit="$(git -C "$target_dir" rev-parse HEAD)"
observed_subtree="$(git -C "$target_dir" rev-parse "HEAD:$subtree_path")"

if [[ "$observed_commit" != "$commit_sha" ]]; then
  echo "Commit verification failed: $observed_commit" >&2
  exit 1
fi
if [[ "$observed_subtree" != "$subtree_sha" ]]; then
  echo "Subtree verification failed: $observed_subtree" >&2
  exit 1
fi

echo "$target_dir"
