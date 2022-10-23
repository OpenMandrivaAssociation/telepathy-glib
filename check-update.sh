#!/bin/sh
# 0.99 is actually a dead branch that is much older than 0.24
curl -L https://telepathy.freedesktop.org/releases/telepathy-glib/ 2>/dev/null |grep '\.tar\.gz"' |sed -e 's,\.tar\.gz".*,,;s,.*-,,' |grep -v 0.99 |sort -V |tail -n1
