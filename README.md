# Infinidat-InfiniBox-filesystems-snapshotting
What it for:
Doing snapshots of specific filesystems (NFS) on InfiniBox once per day, locking snapshots for some time, removing old snapshots with expired locking.

What it does:
When launched, it checks for snapshots for file systems from the list (configurable) on a given day of the week and deletes them.
After that, it creates a new one and locks it for 6 days (configurable)
Code can be easily changed to do snapshots of block devices instead of filesystems.

How it can be used:
It should be run once a day from cron or from a script. As the result you will get seven snapshots for seven days to restore information for previous periods. If you lock snapshots for a longer period, then there will be more of them, for a greater number of days. If you change snapshot name to include not only date, but also time, you cah run it many times per day to get as much snapshots as you want. As the lock expires, the script will delete all expired snapshots for that day. Be careful with locking period.

To work, you need a user on the storage system. I recommend creating a separate pool on the storage system, placing file systems there, making a user with pool_admin rights and giving him rights only to this pool.
