Summary:	GNOME PDF Viewer
Summary(pl):	Przegl±darka PDF-ów dla GNOME
Name:		gpdf
Version:	0.122
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	9119f13bb6ef6d4b20c1870efb392656
Patch0:		%{name}-libgnomeprint.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.5.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.5.6
BuildRequires:	gtk+2-devel >= 2.3.0
BuildRequires:	libbonoboui-devel >= 2.5.0
BuildRequires:	libglade2-devel >= 2.3.0
BuildRequires:	libgnomeprintui-devel >= 2.5.0
BuildRequires:	libgnomeui-devel >= 2.5.0
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPDF is an open source viewer for Portable Document Format (PDF)
files.  (These are also sometimes also called 'Acrobat' files, from
the name of Adobe's PDF software.)

%description -l pl
GPDF to wolnodostêpna przegl±darka do plików PDF (Portable Document
Format; zwanych te¿ czasem plikami "Acrobata" od nazwy oprogramowania
do plików PDF firmy Adobe).

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-schemas-install \
	--enable-a4-paper \
	--enable-multithreaded

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
