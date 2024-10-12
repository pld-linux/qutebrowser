%define		qtver	6

Summary:	A keyboard-driven, vim-like browser based on PyQt6
Name:		qutebrowser
Version:	3.3.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	https://github.com/qutebrowser/qutebrowser/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3aea39613bd6916a37a3df8524d60117
URL:		https://www.qutebrowser.org/
BuildRequires:	python3 >= 1:3.8.0
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Gui >= %{qtver}
Requires:	Qt6Network >= %{qtver}
Requires:	Qt6OpenGL >= %{qtver}
Requires:	Qt6PrintSupport >= %{qtver}
Requires:	Qt6Qml >= %{qtver}
Requires:	Qt6Sql >= %{qtver}
Requires:	Qt6Sql-sqldriver-sqlite3 >= %{qtver}
Requires:	Qt6WebEngine >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
Requires:	bash
Requires:	hicolor-icon-theme
Requires:	python3 >= 1:3.8.0
Requires:	python3-modules >= 1:3.8.0
Requires:	python3-PyQt6
Requires:	python3-PyQt6-WebEngine
Requires:	python3-PyYAML
Requires:	python3-devel-tools
Requires:	python3-jinja2
Suggests:	python3-adblock
Suggests:	python3-pygments
Obsoletes:	qutebrowser-userscripts < 2.4.0-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qutebrowser is a keyboard-focused browser with a minimal GUI. It's
based on Python, PyQt6 and QtWebEngine and free software, licensed
under the GPL. It was inspired by other browsers/addons like dwb and
Vimperator/Pentadactyl.

%package userscript-add-nextcloud-bookmarks
Summary:	qutebrowser userscript: Create bookmarks in Nextcloud's Bookmarks app
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	python3-PyQt6
Requires:	python3-modules
Requires:	python3-requests

%description userscript-add-nextcloud-bookmarks
qutebrowser userscript: Create bookmarks in Nextcloud's Bookmarks app.

%package userscript-add-nextcloud-cookbook
Summary:	qutebrowser userscript: Add recipes to Nextcloud's Cookbook app
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	python3-PyQt6
Requires:	python3-modules
Requires:	python3-requests

%description userscript-add-nextcloud-cookbook
qutebrowser userscript: Add recipes to Nextcloud's Cookbook app.

%package userscript-dmenu
Summary:	qutebrowser userscript: Pipes history, quickmarks, and URL into dmenu
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	dmenu
Requires:	grep
Requires:	sed

%description userscript-dmenu
qutebrowser userscript: Pipes history, quickmarks, and URL into dmenu.

%package userscript-format-json
Summary:	qutebrowser userscript: Pretty prints current page's JSON code in other tab
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/pygmentize
Requires:	jq

%description userscript-format-json
qutebrowser userscript: Pretty prints current page's JSON code in
other tab.

%package userscript-getbib
Summary:	qutebrowser userscript: Scraping the current web page for DOIs and downloading corresponding bibtex information
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	python3-modules

%description userscript-getbib
qutebrowser userscript: Scraping the current web page for DOIs and
downloading corresponding bibtex information.

%package userscript-keepassxc
Summary:	qutebrowser userscript: Insert credentials from open KeepassXC database using keepassxc-browser protocol
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	keepassxc
Requires:	python3-PyNaCl
Requires:	python3-modules
Suggests:	gnupg2

%description userscript-keepassxc
qutebrowser userscript: Insert credentials from open KeepassXC
database using keepassxc-browser protocol.

%package userscript-kodi
Summary:	qutebrowser userscript: Play videos in Kodi
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	/bin/awk
Requires:	bash
Requires:	curl

%description userscript-kodi
qutebrowser userscript: Play videos in Kodi.

%package userscript-open-download
Summary:	qutebrowser userscript: Opens a rofi menu with all files from the download directory and opens the selected file
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bash
Requires:	grep
Requires:	rofi
Requires:	sed
Requires:	xdg-utils

%description userscript-open-download
qutebrowser userscript: Opens a rofi menu with all files from the
download directory and opens the selected file.

%package userscript-openfeeds
Summary:	qutebrowser userscript: Opens all links to feeds defined in the head of a site
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	python3-bs4
Requires:	python3-modules

%description userscript-openfeeds
qutebrowser userscript: Opens all links to feeds defined in the head
of a site.

%package userscript-pass
Summary:	qutebrowser userscript: Insert login information using pass
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	password-store
Requires:	python3-modules
Requires:	python3-tldextract
Suggests:	rofi

%description userscript-pass
qutebrowser userscript: Insert login information using pass.

%package userscript-password-fill
Summary:	qutebrowser userscript: Find a username/password entry and fill it with credentials
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	/bin/awk
Requires:	bash
Requires:	gnupg2
Requires:	grep
Requires:	sed
Requires:	zenity

%description userscript-password-fill
qutebrowser userscript: Find a username/password entry and fill it
with credentialsgiven by the configured backend (currently only pass)
for the current website.

%package userscript-qr
Summary:	qutebrowser userscript: Show a QR code for the current webpage via qrencode
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bash
Requires:	qrencode

%description userscript-qr
qutebrowser userscript: Show a QR code for the current webpage via
qrencode.

%package userscript-qutedmenu
Summary:	qutebrowser userscript: Handle open -s && open -t with dmenu
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bash
Requires:	dmenu

%description userscript-qutedmenu
qutebrowser userscript: Handle open -s && open -t with dmenu.

%package userscript-ripbang
Summary:	qutebrowser userscript: Adds DuckDuckGo bang as searchengine
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	python3-modules
Requires:	python3-requests

%description userscript-ripbang
qutebrowser userscript: Adds DuckDuckGo bang as searchengine.

%package userscript-rss
Summary:	qutebrowser userscript: Keeps track of URLs in RSS feeds and opens new ones
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	curl
Requires:	grep

%description userscript-rss
qutebrowser userscript: Keeps track of URLs in RSS feeds and opens new
ones.

%package userscript-taskadd
Summary:	qutebrowser userscript: Adds a task to taskwarrior
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bash
Requires:	taskwarrior

%description userscript-taskadd
qutebrowser userscript: Adds a task to taskwarrior.

%package userscript-view-in-mpv
Summary:	qutebrowser userscript: Views the current web page in mpv
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bash
Requires:	mpv

%description userscript-view-in-mpv
qutebrowser userscript: Views the current web page in mpv.

%prep
%setup -q

grep -r '#!.*env bash' -l . | xargs %{__sed} -i -e '1 s,#!.*env bash.*,#!/bin/bash,'
grep -r '#!.*env python' -l . | xargs %{__sed} -i -e '1 s,#!.*env python.*,#!%{__python3},'
grep -r '#!.*env node' -l . | xargs %{__sed} -i -e '1 s,#!.*env node.*,#!/usr/bin/node,'

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__make} -f misc/Makefile install PYTHON=/bin/true DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

# requires unpackaged 1password-cli (https://developer.1password.com/docs/cli/)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/qute-1pass
# requires unpackaged castnow (https://github.com/xat/castnow)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/cast
# requires unpackaged Bitwarden CLI (https://bitwarden.com/help/cli/)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/qute-bitwarden
# requires unpackaged pykeepass (https://pypi.org/project/pykeepass/)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/qute-keepass
# requires unpackaged lastpass-cli (https://github.com/lastpass/lastpass-cli)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/qute-lastpass
# requires unpackaged python-readability or breadability
# (https://github.com/buriy/python-readability https://github.com/bookieio/breadability)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/readability
# requires unpackaged node module mozilla/readability (https://github.com/mozilla/readability)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/readability-js
# requires unpackaged stem (https://stem.torproject.org/)
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qutebrowser/userscripts/tor_identity

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README.asciidoc
%attr(755,root,root) %{_bindir}/qutebrowser
%{py3_sitescriptdir}/qutebrowser
%{py3_sitescriptdir}/qutebrowser-%{version}-py*.egg-info
%{_desktopdir}/org.qutebrowser.qutebrowser.desktop
%{_iconsdir}/hicolor/*x*/apps/qutebrowser.png
%{_iconsdir}/hicolor/scalable/apps/qutebrowser.svg
%{_mandir}/man1/qutebrowser.1*
%{_datadir}/metainfo/org.qutebrowser.qutebrowser.appdata.xml
%dir %{_datadir}/qutebrowser
%dir %{_datadir}/qutebrowser/scripts
%{_datadir}/qutebrowser/scripts/*.js
%attr(755,root,root) %{_datadir}/qutebrowser/scripts/*.py
%attr(755,root,root) %{_datadir}/qutebrowser/scripts/*.sh
%dir %{_datadir}/qutebrowser/userscripts

%files userscript-add-nextcloud-bookmarks
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/add-nextcloud-bookmarks

%files userscript-add-nextcloud-cookbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/add-nextcloud-cookbook

%files userscript-dmenu
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/dmenu_qutebrowser

%files userscript-format-json
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/format_json

%files userscript-getbib
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/getbib

%files userscript-keepassxc
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/qute-keepassxc

%files userscript-kodi
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/kodi

%files userscript-open-download
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/open_download

%files userscript-openfeeds
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/openfeeds

%files userscript-pass
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/qute-pass

%files userscript-password-fill
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/password_fill

%files userscript-qr
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/qr

%files userscript-qutedmenu
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/qutedmenu

%files userscript-ripbang
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/ripbang

%files userscript-rss
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/rss

%files userscript-taskadd
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/taskadd

%files userscript-view-in-mpv
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/view_in_mpv
