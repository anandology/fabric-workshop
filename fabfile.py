from fabric.api import env, task, run, sudo

env.user = "vagrant"
env.password = "vagrant"
env.hosts = ["192.168.50.10", "192.168.50.11"]

@task
def hostname():
    """Prints hostname
    """
    run('hostname')

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
def createdb(name):
    """Task to create a database on all nodes.
    """
    # creates a database with given name on all the nodes
    run("createdb " + name)
