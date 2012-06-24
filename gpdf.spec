Summary:	GNOME PDF Viewer
Summary(pl):	Przegl�darka PDF-�w dla GNOME
Name:		gpdf
Version:	0.100
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.100/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 1.2.1-10
BuildRequires:	bonobo-activation-devel >= 2.1.0-3
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	rpm-build >= 4.1-8.2
BuildRequires:	scrollkeeper
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	bonobo-activation >= 2.1.0-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPDF is an open source viewer for Portable Document Format (PDF)
files.  (These are also sometimes also called 'Acrobat' files, from
the name of Adobe's PDF software.)

%description -l pl
GPDF to wolnodost�pna przegl�darka do plik�w PDF (Portable Document
Format; zwanych te� czasem plikami "Acrobata" od nazwy oprogramowania
do plik�w PDF firmy Adobe).

%prep
%setup -q

%build
%configure

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
%{_datadir}/application-registry/gpdf.applications
%{_datadir}/applications/gpdf.desktop
%{_datadir}/gnome-2.0/ui/gpdf*
%{_datadir}/gpdf
%{_datadir}/mime-info/gpdf.keys
%{_libdir}/bonobo/servers/*
%{_pixmapsdir}/*
