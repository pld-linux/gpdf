Summary:	GNOME PDF Viewer
Summary(pl):	Przegl±darka PDF-ów dla GNOME
Name:		gpdf
Version:	2.7.91
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	167494c9f75876f1ec8173d227a7cbe6
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.7.92
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.7.92
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libbonoboui-devel >= 2.6.1
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.7.1
BuildRequires:	libgnomeui-devel >= 2.7.92
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPDF is an open source viewer for Portable Document Format (PDF)
files.

%description -l pl
GPDF to wolnodostêpna przegl±darka do plików PDF (Portable Document
Format).

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gnome-pdf-viewer
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/application-registry/gpdf.applications
%{_desktopdir}/gpdf.desktop
%{_datadir}/gnome-2.0/ui/gpdf*
%{_datadir}/%{name}
%{_datadir}/mime-info/gpdf.keys
%{_libdir}/bonobo/servers/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/*
