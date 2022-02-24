from invoke import task
import os

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    os.chdir(".src")
    ctx.run("pytest")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coveage html")

@task
def lint(ctx):
    ctx.run("pylint src")
