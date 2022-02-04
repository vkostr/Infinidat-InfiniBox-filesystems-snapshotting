# Infinidat-InfiniBox-filesystems-snapshotting
To work, you need a user on the storage system. I recommend creating a separate pool on the storage system, placing file systems there, making a user with pool_admin rights and giving him rights only to this pool.

What does it do:
When launched, it checks for snapshots for file systems from the list (configurable) on a given day of the week and deletes them.
After that, it creates a new one and locks it for 6 days (configurable)

How it can be used - run once a day from cron or from a script that backups the database.
What happens in the end is the availability of seven snapshots in seven days to restore information for previous periods. If you lock snapshots for a longer period, then there will be more of them, for a greater number of days. As the block expires, the script will delete them.
