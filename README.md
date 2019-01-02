# Workflowy 2 Org-Mode

A script for converting Workflowy lists to .org files so they can be used in Emacs org-mode. Requires Python 2.

## Usage

Download your Workflowy list by going to "Export All" and choosing "Plain text". Run `python workflowy2org.py`.

## Why?

This was created for my personal need, but I hope it will be useful for others as well.

org-mode in Emacs has many advantages over Workflowy:

* Workflowy is a proprietary service, while org-mode uses simple plaintext which never becomes obsolete.
* Workflowy can disappear without a trace at any moment.
* You can keep .org files locally. Workflowy is a web service and requires an Internet connection.
* You can back up your .org files or sync them to other devices automatically. Workflowy lists have to be backed up manually.
* org-mode leverages Emacs functionality and keybindings, allowing you to take notes and update the hierarchy structure quickly and intuitively if you know Emacs.
* org-mode is much more flexible, configurable, and has more features.

## Limitations

* Does not (yet) convert workflowy-style tags (#example) to org-style tags (:example:).
* The method described in the [Usage section](#Usage) does not preserve formatting (bold, italics, etc.).
