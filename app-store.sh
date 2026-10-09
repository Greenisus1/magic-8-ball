#!/bin/bash
# pi-app-store: 1
# pi-app-store-category: games
# pi-app-store-description: Random classic-style 8-ball answers, no AI or translation.
set -eu
cd -- "$(dirname -- "$0")"
case "${1:-}" in
 install) python3 -c 'from pathlib import Path;compile(Path("eightball.py").read_bytes(), "eightball.py", "exec")' ;;
 run) shift; exec python3 eightball.py "$@" ;;
 *) echo 'Use: bash app-store.sh install OR bash app-store.sh run';exit 1 ;;
esac
