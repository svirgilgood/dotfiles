# dotfiles

## Setting up Java to Work with Sway

There are four issues that need to be addressed in Java. 
1. Theme. Java uses a settings daemon. Gnome has a settings demon that java can use, but Windows Managers don't usually have these built in.
2. Nonereparenting. Menus in java under sway won't stay open unless you set a variable to let Java know this is a Nonereparenting. 
3. Openwebstart needs to be configured properly to use the correct version of java.
4. Run the app with the `javaws` command.

### Install xsettingsd 

For getting java apps to display correctly you need a settings daemon. Gnome has a built in one, but you 
may need to install xsettingsd and enable it. This allows Java apps to be able to see how to render fonts 
and which ones to use. 

This is only for users, so use the `--user` flag in the systemctl daemon

1. Set the config:
`~/.config/xsettingsd/xsettingsd.conf`
```
Xft/AntiAlias   1
#Xft/DPI         98304
Xft/Hinting     1
Xft/HintStyle   "hintfull"
Xft/lcdfilter   "lcddefault"
Xft/RGBA        "rgb"
```

I commented out the DPI setting, this seemed to pass through pretty well. 
See [xsettingsd in the arch wiki for details](https://wiki.archlinux.org/title/Xsettingsd) for details about the config.

1. Set the necessary variables:
`systemctl --user import-environment DISPLAY XAUTHORITY`
 The `XAUTHORITY` variable needs to be set in .profile or .env (for example `export XAUTHORITY="$HOME/.Xauthority` in .zshenv)

1. Start the service:
`system --user start xsettingsd.service`


### Install Necessary JRE 

`# pacman -S jre8-openjdk` 

### Set Import Java Variables 

Wayland doesn't quite register some clicks the same way x11 does. 

If the java menu's won't stay open, set the environmental variable:

`export _JAVA_AWT_WM_NONREPARENTING=1`


### Install openwebstart

Openwebstart is available trough the AUR. 

`yay -S openbwebstart-bin`

### Set the right version of Java 

Use `itw-settings` (this is a command that comes with `openwebstart`) to set the local version of java. make sure that it is set to only look for local versions of java. 


### Run the app:

`javaws "http://url/for/jnlp/file`



