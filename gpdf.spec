Summary:	GNOME PDF Viewer
Summary(pl.UTF-8):	Przeglądarka PDF-ów dla GNOME
Name:		gpdf
Version:	2.10.0
Release:	4
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/gpdf/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	9278cd3b9d06e3b1d364452f0e512fa9
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-CAN-2005-2097.patch
Patch2:		%{name}-cve-2006-0301.patch
Patch3:		%{name}-classes.patch
Patch4:		%{name}-as_needed.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.10.0
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPDF is an open source viewer for Portable Document Format (PDF)
files.

%description -l pl.UTF-8
GPDF to wolnodostępna przeglądarka do plików PDF (Portable Document
Format).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-a4-paper \
	--enable-multithreaded
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -rf $RPM_BUILD_ROOT%{_datadir}/{mime-info,application-registry}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install gpdf.schemas
%update_desktop_database_post

%preun
%gconf_schema_uninstall gpdf.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gnome-pdf-viewer
%{_sysconfdir}/gconf/schemas/*.schemas
%{_desktopdir}/gpdf.desktop
%{_datadir}/gnome-2.0/ui/gpdf*
%{_datadir}/%{name}
%{_libdir}/bonobo/servers/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/*
