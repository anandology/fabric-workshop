from fabric.api import env, task, run, sudo

env.user = "vagrant"
env.password = "vagrant"
env.hosts = ["192.168.50.10", "192.168.50.11"]

@task
def host_type():
    run('uname -s')

@task
def helloworld():
    run("echo hello world")

@task
def root():
    sudo("whoami")
