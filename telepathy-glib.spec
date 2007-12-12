Name:           telepathy-glib
Version:        0.7.0
Release:        %mkrel 1
Summary:        A glib utility library for the telepathy framework

Group:          Networking/Instant messaging
License:        LGPL
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
#Source1:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz.asc
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  glib2-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  libxslt-proc
BuildRequires:  python-devel

Requires:       telepathy-filesystem

%description

A glib utility library for the telepathy framework

%files
%defattr(-,root,root,-)
%{_includedir}/telepathy-1.0/telepathy-glib/*.h
%{_includedir}/telepathy-1.0/telepathy-glib/_gen/*.h
%{_libdir}/*
%{_datadir}/gtk-doc/html/telepathy-glib/*

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure
%make


%install
rm -rf %buildroot
make install DESTDIR=%buildroot


%clean
rm -rf %buildroot
