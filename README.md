# Spotify installer for openSUSE LEAP 42.2 (and 42.1)

This script avoids the need to illegally redistribute Spotify binaries
by downloading the Linux client `.deb` from
[repository.spotify.com](http://repository.spotify.com/pool/non-free/s/spotify/),
converting it to `.rpm` format, and then installing it along with some
evil hacks to provide the necessary libraries where Spotify expects
them to be.

## Current status

Currently
~~[this code is broken](https://github.com/aspiers/opensuse-spotify-installer/issues),
however
[work is underway to fix it](https://github.com/aspiers/opensuse-spotify-installer/pull/37).~~

**This repository is a [fork from aspiers](https://github.com/aspiers/opensuse-spotify-installer) that right now looks unmaintained. I made an effort to fix the issues, getting the installer work again with a minor addition to the usage process (see step 0 in [How to use](#how-to-use) below).**

You could also try
[`spotify-make`](https://github.com/leamas/spotify-make).  The hope is
that we ultimately reach
[a unified solution](https://github.com/aspiers/opensuse-spotify-installer/pull/37#issuecomment-95361176)
which reuses the combined efforts of as many people as possible, in an
efficient and collaborative manner.

## How to use

1. Clone the repository using `git clone https://github.com/janwillhaus/opensuse-spotify-installer.git`
2. Run the installer script as non-root user: `./install-spotify.sh`

The installer uses `sudo` for operations which require root privileges, so
you may be prompted for a password during the install.

## Support, bugs, development etc.

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Why not just use the new web-based player?

There's a new browser-based Spotify player accessible via
[https://play.spotify.com/](https://play.spotify.com/) or
[https://apps.facebook.com/get-spotify/](https://apps.facebook.com/get-spotify/).

However, [it does not seem to be generally available yet](http://howto.cnet.com/8301-11310_39-57551372-285/enable-spotifys-web-player-right-now/), and [is missing many features](http://community.spotify.com/t5/Desktop-Linux/ANNOUNCE-Spotify-0-8-4-for-GNU-Linux/m-p/204364/highlight/true#M1687) compared to the standalone Linux client.

## Credits and thanks

This is not all my own work.  The following people deserve credit and
thanks for some of the code in this installer:

* [Armin](http://community.spotify.com/t5/user/viewprofilepage/user-id/190504) on the Spotify community forums, who wrote the
[original version](http://community.spotify.com/t5/Desktop-Linux/Segfault-on-opensuse-12-2/m-p/161048/highlight/true#M1331).
* [Marguerite Su](https://github.com/marguerite) who provided an initial `.spec` file and helped eventually convince me it was worth moving away from `alien`.

Huge thanks also to the relatively anonymous Spotify employees such as
[parbo](http://community.spotify.com/t5/user/viewprofilepage/user-id/23361)
who have been donating some of their free time to make the Linux
client available.  *No* thanks go to Spotify middle/upper management
for consistently refusing to invest the small amount of resources
required to even acknowledge their Linux-based customers, let alone
support them.

## License

This installer does *not* contain any material whatsoever copyrighted
by Spotify:

*   `install-spotify.sh` is a derivative of Armin's original version which
    he posted it without any copyright notice, so I unless I hear
    otherwise I'll assume it's in the public domain.
*   `spotify-client.spec` is a derivative of Marguerite Su's original
    `spotify.spec`, the header of which seems to imply that it's
    MIT-licensed (since the pristine package the header refers to is
    either Spotify or non-existent, depending on how you look at it).
*   `spotify-installer.spec` is all my work.

Therefore I think it's fair to say the overall license is MIT (i.e.
less ambiguously, the X11 license).

## Why is this script here on github?

I hope it's kind of obvious from the above.  But since you
got me on the soapbox ...

`<rant length="very long">`

Web forums breed endless technological misery.  They are bloated,
slow, clunky quagmires which result in long meandering threads of
unstructured communication.  Trying to install Spotify after every
distribution upgrade typically involves the following steps:

1. google for something like 'spotify opensuse 12.2'
2. wade through a *huge* number of hits from web forum threads or blog post or wiki page,
   many of which are too old to be useful
3. select the most promising looking hit
4. wade through a long forum thread or web page
5. re-live other people's trial-and-error experiences
6. realise that most people on this thread don't really know what they're doing
   and no-one fully figured it out
7. repeat steps 3--6 a few times
8. observe that every man and his dog has come up with their own
   partial solution which is similar but slightly different to the next
   person's, due to various gotchas which apply in some cases but not others
9. scream "I don't care, I just want the ****ing thing to work!" a few times
10. mentally recombine several different nuggets of information
11. experiment a bit

... and eventually maybe you get it to work.  If you're really lucky
Spotify might only segfault occasionally!

(If I was [rms](http://en.wikipedia.org/wiki/Richard_Stallman), now
would be the time to point out that this is inevitable karma for
trying to use [freedom-denying software](http://www.gnu.org/philosophy/);
sadly I do not possess as much integrity as him though.)

I've been working closely with Linux since 1995 and even with a lot of
experience I find process this painful and frustrating every time.  So
I can't imagine how annoyed Linux newbies must get when they want to
do something as conceptually simple as installing Spotify on an
rpm-based distro, and find that they have to struggle through this
crap.  It flies against *all* conventional wisdom regarding best
practices in software development and deployment.

Going through this yet again after this latest upgrade to openSUSE
12.2 was the straw that broke the camel's back (Fedora 16 was the
penultimate straw...)  So let's take a stand.  We can and will do
better!  Barring an unexpected miracle from Spotify management where
they suddenly decide to stop ignoring their Linux user base, the
solution is relatively simple.  We just need to treat the problem with
respect, i.e. just like any other free or open source software project
out there - it deserves standard best practices.  That means an
automated deployment mechanism which is tracked properly using
decentralized version control, a bug tracker, and a collaborative
platform which allows anyone to chip in and help in a *structured*
fashion.  Fortunately github is totally mind-bendingly awesome at
this, and free!  So let's use it!

`</rant>`
