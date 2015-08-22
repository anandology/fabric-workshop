from fabric.api import env, task, run, sudo, cd, local, get

env.user = "vagrant"
env.password = "vagrant"
#env.hosts = ["192.168.50.10", "192.168.50.11"]

@task
def even():
    env.hosts = ["192.168.50.10"]

@task
def odd():
    env.hosts = ["192.168.50.11"]

@task
def hostname():
    """Prints hostname
    """
    print "running hostname task"
    repr(run('hostname'))

@task
def hello():
    """Prints hello world
    """
    run("echo hello world")

@task
def root():
    """Runs something as root"""
    sudo("whoami")

@task
def sleep():
    """Sleeps for 5 seconds"""
    run("sleep 5")

@task
def touch(filename="/tmp/a.txt"):
    """touchs a file on all nodes."""
    run("touch " + filename)

@task
def createdb(name):
    """Task to create a database on all nodes.
    """
    # creates a database with given name on all the nodes
    run("createdb " + name)


@task
def backupdb():
    run("mkdir -p /tmp/backups")
    with cd("/tmp/backups"):
        run("pg_dumpall | gzip > db-backup.gz")

@task
def sync_backups():
    local("mkdir -p backups/")
    get("/tmp/backups/db-backup.gz", "backups/%(host)s-db-backup.gz")
    #get("/tmp/backups", "backups/%(host)s/")
    #run("scp /tmp/backups/db-backup.gz backupserver:/tmp/as")
