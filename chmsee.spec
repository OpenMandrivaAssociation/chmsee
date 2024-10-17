%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	A Gtk+2 based CHM viewer
Name:		chmsee
Version:	1.3.1.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://code.google.com/p/chmsee/
Source0:	http://chmsee.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	intltool
BuildRequires:	chmlib-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxul)

Requires: libxulrunner = %{xulrunner_version}

%description
ChmSee is an HTML Help viewer for Unix/Linux. It is based on CHMLIB
and use Gtk2+ as frontend toolkit. Because of using gecko as HTML
rendering engine, ChmSee can support rich features of modern HTML
page, such as CSS and JavaScript.

%prep
%setup -q

%build
%cmake 
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/chmsee
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/*/*

