%define major 0
%define api 0.12
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	A glib utility library for the telepathy framework
Name:		telepathy-glib
Version:	0.24.1
Release:	1
Group:		Networking/Instant messaging
License:	LGPLv2+
URL:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		telepathy-glib-0.11.11-missing-file.patch

BuildRequires:	gtk-doc
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	vala-devel >= 0.12
BuildRequires:	vala-tools

%description
%{name} is a glib utility library for the telepathy framework.

%package -n %{libname}
Summary:	A glib utility library for the telepathy framework
Group:		System/Libraries
Requires:	telepathy-filesystem
%rename		%{name}

%description -n %{libname}
%name is a glib utility library for the telepathy framework.

%package -n %{devname}
Summary:	A glib utility library for the telepathy framework
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} is a glib utility library for the telepathy framework.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x \
	--enable-vala-bindings \
	--disable-static

%make PYTHON=python2

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/libtelepathy-glib.so.%{major}*
%{_libdir}/girepository-1.0/TelepathyGLib-%{api}.typelib

%files -n %{devname}
%{_libdir}/libtelepathy-glib.so
%{_datadir}/gir-1.0/TelepathyGLib-%{api}.gir
%dir %{_includedir}/telepathy-1.0/
%dir %{_includedir}/telepathy-1.0/telepathy-glib/
%dir %{_includedir}/telepathy-1.0/telepathy-glib/_gen
%{_includedir}/telepathy-1.0/telepathy-glib/*.h
%{_includedir}/telepathy-1.0/telepathy-glib/_gen/*.h
%{_datadir}/gtk-doc/html/telepathy-glib/
%{_libdir}/pkgconfig/telepathy-glib.pc
%{_datadir}/vala/vapi/telepathy-glib.deps
%{_datadir}/vala/vapi/telepathy-glib.vapi
