# Pexe - Passwords Everywhere eXtreamily Easy

Pexe is, in a way, a password manager.

It is extremily light weight, has but 50-60 lines of code.

Pexe is not a new invention, it is not even a product, just an acronym name, because it got to have a name right?

## Why use hash passwords

- Password managers including well known ones, have a record of leaking passwords
- Hash generated passwords are not stored anywhere
- Hash generated passwords are basically easily available on almost ALL devices
- Enforces always strong passwords, because all your passwords will be cryptographically pseudo random
- If you do remember parts of your password, one way to recover it could be to create a script that just tries a bunch of stuff and looks for hashes that match parts of a password that you remember.

## Downside

- No recovery if forget your master password
- May be less userfriendly as a simple CLI
- Trust in the implementation, e.g. pyperclip in python
- No password or secret sharing
- Your familiy and friends will get very annoyed with you when they want to use your Netflix account on the TV

## Security

How secure is this?

TL;DR: more secure than your average password manager for reasons mentioned above

Longer answer is: As secure as the least secure of one of these:
- Strength of HMAC-SHA256: never compromised, considered impossible to crack as of april 2025
- Your means of storing / saving the master password


## Usage

Use a naming convention to ensure you get the right password. For example:

Email:
```
<my email>+<tag>
```

Site login with user name
```
<name of site>/<my user>+<tag>
```

Site login with mail (reccomended as mail is often easier to remember than usernames)
```
<name of site>/<my mail>+<tag>
```

Named secret
```
<name of secret>
```

etc

example

```
github/kevin17833+25
```

You should use a tag, because this is how you would change your password every now and then. 25 could refer to the year.

To copy the password to clipboard, you would then do:

```
python pexe.py github/kevin17833+25
```

Enter secret, e.g. password123 (for test purpose)

output
```
SYyB6jx8

Password has been copied to your clipboard.
```

SYyB6jx8 is small piece of the hash of your password without a "domain" or seed, to give a hint to whether you have written the password correctly.

This is printed out, because as you need to register yourself at new sites with a password, this would indicate that your master password entered was correct.

If you entered it wrong, a different text, one that you would not recognize would show up.