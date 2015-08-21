from fabric.api import task, run

@task
def host_type():
    run('uname -s')

@task
def helloworld():
    run("echo hello world")

@task
def root():
    sudo("whoami")
