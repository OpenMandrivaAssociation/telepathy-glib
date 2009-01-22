%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name
Name:           telepathy-glib
Version:        0.7.23
Release:        %mkrel 1
Summary:        A glib utility library for the telepathy framework

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  glib2-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  libxslt-proc
BuildRequires:  python-devel

%description
%name is a glib utility library for the telepathy framework.

%package -n %libname
Group: System/Libraries
Summary: A glib utility library for the telepathy framework
Provides: %name
Obsoletes: %name
Requires:       telepathy-filesystem

%description -n %libname
%name is a glib utility library for the telepathy framework.

%package -n %develname
Group: Development/C
Summary: A glib utility library for the telepathy framework
Requires: %libname = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %develname
%name is a glib utility library for the telepathy framework.

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libtelepathy-glib.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/libtelepathy-glib.la
%{_libdir}/libtelepathy-glib.so
%dir %{_includedir}/telepathy-1.0/
%dir %{_includedir}/telepathy-1.0/telepathy-glib/
%{_includedir}/telepathy-1.0/telepathy-glib/*.h
%{_includedir}/telepathy-1.0/telepathy-glib/_gen/*.h
%{_datadir}/gtk-doc/html/telepathy-glib/
%_libdir/pkgconfig/telepathy-glib.pc

#--------------------------------------------------------------------

%prep
%setup -q
#%patch -p1 -b .pkgconfig

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std
rm -f %buildroot%{_libdir}/libtelepathy-glib.a

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif
