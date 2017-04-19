#
# spec file for package spotify
#
# Copyright (c) 2012 Marguerite Su, Adam Spiers
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           spotify-client
Version:        1.0.53.758.gde3fc4b2
License:        Commercial
Summary:        Desktop client for Spotify streaming music service
Url:            http://www.spotify.com/download/previews/
Group:          Productivity/Multimedia/Sound/Players
%ifarch x86_64
Release:        33
Source0:        spotify-client_%{version}-%{release}_amd64.deb
%else
Release:        34
Source0:        spotify-client_%{version}-%{release}_i386.deb
%endif
NoSource:       0
%if 0%{?suse_version}
Requires:       mozilla-nss
Requires:       mozilla-nspr
Requires:       libopenssl1_0_0
Requires:       libpng12-0
Recommends:     libmp3lame0
Recommends:     ffmpeg
%endif

# not currently tested on Fedora or Mandriva, but leaving
# these here in case anyone wants to step up and do it :)
%if 0%{?fedora_version}
Requires:       nss
Requires:       nspr
Requires:       openssl >= 1.0.0
%endif
%if 0%{?mandriva_version}
Requires:       libnss3
Requires:       libnspr4
Requires:       libopenssl1.0.0
Conflicts:      libopenssl0.9.8
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Spotify is a "Freemium" proprietary, DRM-restricted digital music
service that gives you access to millions of songs.

It includes the following features:

- Custom playlists
- Last.fm integration
- Customized radio dynamically generated to the user's tastes
- Social media integration with Facebook and Twitter
- 3rd-party applications integrated into the client

%prep
%setup -T -c %{name}_%{version}
# unpack deb
ar -x %{SOURCE0}
# unpack data
tar -xf data.tar.gz
# remove used files
rm data.tar.gz control.tar.gz debian-binary

%define _use_internal_dependency_generator 0
%define __find_requires %_builddir/%{name}-%{version}/find-requires.sh
cat >%__find_requires <<'EOF'
#!/bin/sh
EOF
chmod +x %__find_requires

%build
# no need to build

%install
mv usr %{buildroot}
%define spotifydir /usr/share/spotify

mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/../%{name}/* %{buildroot}%{_docdir}/%{name}/
cat >%{buildroot}%{_docdir}/%{name}/README <<EOF
This package was built by the openSUSE Spotify installer; see

    https://github.com/janwillhaus/opensuse-spotify-installer

for more information.
EOF

%post
/sbin/ldconfig

for icon in $(ls -1 %{spotifydir}/icons/spotify-linux-*.png); do
    size="${icon##*/spotify-linux-}"
    xdg-icon-resource install --noupdate --size "${size%.png}" "$icon" "spotify-client" || true
done

xdg-desktop-menu install --novendor "%{spotifydir}/spotify.desktop" || true
update-menus || true


%preun
# nothing to do here.

%postun
if [ "$1" = 0 ]; then
    /sbin/ldconfig
fi

for icon in $(ls -1 $spotifyPath/icons/spotify-linux-*.png); do
    size="${icon##*/spotify-linux-}"
    xdg-icon-resource uninstall --noupdate --size "${size%.png}" "$icon" "spotify-client" || true
done

xdg-desktop-menu uninstall --novendor "spotify.desktop" || true
update-menus || true


%files
%defattr(-,root,root)
%spotifydir
%doc %{_docdir}/%{name}
%{_bindir}/spotify

%changelog
* Tue Dec 27 2016 Jan Willhaus <mail@janwillhaus.de>
- update to 1.0.45 (moved to /usr/share/spotify)

* Sat Jan 05 2013 Adam Spiers <spotify-on-opensuse@adamspiers.org>
- add README

* Sat Jan 05 2013 Adam Spiers <spotify-on-opensuse@adamspiers.org>
- update to 0.8.8 (moved to /opt)
- rename to spotify-client for consistency with original Debian package
- use provided register.sh and unregister.sh
- remove need to conflict with libopenssl0_9_8
- fix automatically generated dependencies
- fix XDG categories
- move dedicated library directory to /opt/spotify/spotify-client/lib
- remove spotify-linux-512x512.png since redistribution probably
  violates Spotify copyright
- fix SPOTIFY_CLEAN_CACHE test
- fix passing of multiple arguments to spotify binary

* Mon Aug 20 2012 Marguerite Su <i@marguerite.su> - 0.8.4.103.g9cb117b.260
- initial version with Spotify App support.
- use libopenssl1_0_0 instead of libopenssl0_9_8 to fix a crash and other linkings ready.
- use wrapper to clear cache manually
