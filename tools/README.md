# installation and setup of the website

## Python

chances are that the box has been upgraded, so the python environment probably
needs being reinstalled

### not conda

we are **not using conda** in the linux container

because entering a conda env from a systemd service (or a crontab job) is very awkward
conda activate complains about the shell not being init'ed, but but but it was !

### hence `requirements.txt`

* from a pure fedora41 box
* pip install -f requirements.txt

## update 2025: apache -> caddy

see `/etc/caddy/Caddyfile` for the configuration
no longer need the `apache` user

## from one year to another

### website layout

one can access a specific year - useful during setup

* there is a symlink that points to the current year, e.g. `p24`:
  `/var/www/html/projects-library/`
* tweak `/etc/caddy/Caddyfile`
* replace e.g. `p23` into `p24` in all the files of this repo

### next year


create a new repo like this:

```
mkdir ../ue22-p24-PI
tar -cf - $(git ls-files | grep -v subjects/) | tar -C ../ue22-p24-PI -xf -
cd ../ue22-p24-PI
git init
git add .
git commit -m starter point from previous year
# at this point replace all p23 with p24
mkdir subjects
```

also deal with the logo
