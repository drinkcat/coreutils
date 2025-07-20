# spell-checker:ignore epipe readdir restorecon SIGALRM capget bigtime rootfs enotsup

* tests/tail-2/pipe-f.sh - trapping SIGPIPE is not supported
* tests/misc/seq-epipe.sh - trapping SIGPIPE is not supported
* tests/misc/printf-surprise.sh - trapping SIGPIPE is not supported
* tests/misc/env-signal-handler.sh - trapping SIGPIPE is not supported

* tests/tail-2/inotify-race2.sh - skipped test: breakpoint not hit
* tail-2/inotify-race.sh - skipped test: breakpoint not hit

* tests/rm/rm-readdir-fail.sh - internal test failure: maybe LD_PRELOAD doesn't work?
* tests/rm/r-root.sh - internal test failure: maybe LD_PRELOAD doesn't work?
* tests/df/skip-duplicates.sh - internal test failure: maybe LD_PRELOAD doesn't work?
* tests/df/no-mtab-status.sh - internal test failure: maybe LD_PRELOAD doesn't work?

* tests/cp/nfs-removal-race.sh - LD_PRELOAD was ineffective?

* tests/mv/hardlink-case.sh - failed to create hfs file system

* tests/mkdir/writable-under-readonly.sh - temporarily disabled

* tests/mkdir/smack-root.sh - this system lacks SMACK support
* tests/mkdir/smack-no-root.sh - this system lacks SMACK support
* tests/id/smack.sh - this system lacks SMACK support

* tests/mkdir/selinux.sh - this system lacks SELinux support
* tests/mkdir/restorecon.sh - this system lacks SELinux support
* tests/misc/selinux.sh - this system lacks SELinux support
* tests/misc/chcon.sh - this system lacks SELinux support
* tests/install/install-Z-selinux.sh - this system lacks SELinux support
* tests/install/install-C-selinux.sh - this system lacks SELinux support
* tests/id/no-context.sh - this system lacks SELinux support
* tests/id/context.sh - this system lacks SELinux support
* tests/cp/no-ctx.sh - this system lacks SELinux support
* tests/cp/cp-a-selinux.sh - this system lacks SELinux support

* tests/misc/xattr.sh - failed to set xattr of file

* tests/misc/timeout-group.sh - timeout returned 142. SIGALRM not handled?

* tests/misc/tac-continue.sh - FULL_PARTITION_TMPDIR not defined

* tests/misc/stty-row-col.sh - can't get window size

* tests/misc/sort-h-thousands-sep.sh - The Swedish locale with blank thousands separator is unavailable.

* tests/misc/csplit-heap.sh - this shell lacks ulimit support

* tests/misc/coreutils.sh - multicall binary is disabled

* tests/id/gnu-zero-uids.sh - not running on GNU/Hurd

* tests/du/bigtime.sh - file system cannot represent big timestamps

* tests/df/skip-rootfs.sh - no rootfs in mtab

* tests/df/problematic-chars.sh - insufficient mount/ext2 support
* tests/cp/cp-mv-enotsup-xattr.sh - insufficient mount/ext2 support

* tests/dd/direct.sh - 512 byte aligned O_DIRECT is not supported on this (file) system

* tests/misc/ls-time.sh - skipped test: /usr/bin/touch -m -d '1998-01-15 23:00' didn't work

* tests/misc/stty-pairs.sh - requires controlling input terminal
* tests/misc/stty.sh - requires controlling input terminal
* tests/misc/stty-invalid.sh - requires controlling input terminal

* tests/cp/sparse-perf.sh - insufficient SEEK_DATA support
* tests/cp/sparse-extents.sh - insufficient SEEK_DATA support
* tests/cp/sparse-extents-2.sh - insufficient SEEK_DATA support
* tests/cp/sparse-2.sh - insufficient SEEK_DATA support
