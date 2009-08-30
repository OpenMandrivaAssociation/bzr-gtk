# based on http://cvs.fedora.redhat.com/viewcvs/devel/bzr-gtk/?root=extras
Name:           bzr-gtk
Version:        0.97.0
Release:        %mkrel 1
Summary:        Bazaar plugin for GTK+ interfaces to most Bazaar operations

Group:          Development/Python
License:        GPL
URL:            http://bazaar-vcs.org/bzr-gtk
Source0:	http://edge.launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  python-devel bzr
BuildRequires:  gettext
Requires:       bzr >= 1.0
Requires:       pygtk2.0
Requires:       pygtk2.0-libglade
Requires:	python-cairo
Requires:	python-gtksourceview

%description
bzr-gtk is a plugin for Bazaar that aims to provide GTK+ interfaces to most
Bazaar operations.

%package -n olive
Summary: Graphical frontend to the bazaar revision control system
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description -n olive
Olive aims to be a full-featured graphical frontend for Bazaar.  It will
expose all core functionality of Bazaar in a user-friendly GUI.

%package nautilus
Summary: Nautilus integration for bzr-gtk
Group: Development/Other
Requires: %{name} = %{version}-%{release}
Requires: python-nautilus

%description nautilus
bzr-gtk integration with the nautilus file manager for gnome.

%prep
%setup -q

%build
python setup.py build


%install
rm -rf %{buildroot}
python setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_prefix}/lib/nautilus/extensions-1.0/python/
mv %{buildroot}%{python_sitelib}/bzrlib/plugins/gtk/nautilus* %{buildroot}%{_prefix}/lib/nautilus/extensions-1.0/python/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING README
%py_puresitedir/bzrlib/plugins/gtk/
%py_puresitedir/*egg-info
%{_datadir}/applications/bazaar-properties.desktop
%{_datadir}/applications/bzr-handle-patch.desktop
%{_datadir}/applications/bzr-notify.desktop
%{_datadir}/application-registry/bzr-gtk.applications
%{_datadir}/%{name}
%{_datadir}/pixmaps/bzr-icon-64.png
%{_iconsdir}/hicolor/scalable/emblems/*

%files -n olive
%defattr(-,root,root,-)
%{_bindir}/*
%py_puresitedir/bzrlib/plugins/gtk/olive
%{_datadir}/olive
%{_datadir}/pixmaps/olive-gtk.png
%{_datadir}/applications/olive-gtk.desktop
%{_datadir}/locale/*

%files nautilus
%{_prefix}/lib/nautilus/extensions-1.0/python/*
