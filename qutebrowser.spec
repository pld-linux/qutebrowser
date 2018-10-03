%define		qtver	5.7.1
Summary:	A keyboard-driven, vim-like browser based on PyQt5
Name:		qutebrowser
Version:	1.5.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	https://github.com/qutebrowser/qutebrowser/archive/v%{version}.tar.gz
# Source0-md5:	23d33db8436b439c33a78a25fdee53fb
URL:		https://www.qutebrowser.org/
BuildRequires:	asciidoc
BuildRequires:	python3 >= 3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5OpenGL >= %{qtver}
Requires:	Qt5Sql >= %{qtver}
Requires:	Qt5WebEngine >= %{qtver}
Requires:	bash
Requires:	hicolor-icon-theme
Requires:	python3 >= 3.6
Requires:	python3-PyQt5 >= 5.7.0
Requires:	python3-PyYAML
Requires:	python3-attrs
Requires:	python3-jinja2
Requires:	python3-pyPEG2
Requires:	python3-pygments
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qutebrowser is a keyboard-focused browser with a minimal GUI. It’s
based on Python, PyQt5 and QtWebEngine and free software, licensed
under the GPL. It was inspired by other browsers/addons like dwb and
Vimperator/Pentadactyl.

%prep
%setup -q

grep -r '#!.*env bash' -l . | xargs %{__sed} -i -e '1 s,#!.*env bash.*,#!/bin/bash,'
grep -r '#!.*env python' -l . | xargs %{__sed} -i -e '1 s,#!.*env python.*,#!%{__python3},'

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__make} -f misc/Makefile install PYTHON=/bin/true DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

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
%{_desktopdir}/qutebrowser.desktop
%{_iconsdir}/hicolor/*x*/apps/qutebrowser.png
%{_iconsdir}/hicolor/scalable/apps/qutebrowser.svg
%{_mandir}/man1/qutebrowser.1*
%{_datadir}/metainfo/qutebrowser.appdata.xml
%dir %{_datadir}/qutebrowser
%dir %{_datadir}/qutebrowser/scripts
%{_datadir}/qutebrowser/scripts/*.js
%attr(755,root,root) %{_datadir}/qutebrowser/scripts/*.py
%attr(755,root,root) %{_datadir}/qutebrowser/scripts/*.sh
%dir %{_datadir}/qutebrowser/userscripts
%attr(755,root,root) %{_datadir}/qutebrowser/userscripts/*