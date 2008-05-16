# based on http://cvs.fedora.redhat.com/viewcvs/devel/bzr-gtk/?root=extras
Name:           bzr-gtk
Version:        0.94.0
Release:        %mkrel 2
Summary:        Bazaar plugin for GTK+ interfaces to most Bazaar operations

Group:          Development/Python
License:        GPL
URL:            http://bazaar-vcs.org/bzr-gtk
Source0:        http://samba.org/~jelmer/bzr/bzr-gtk-%{version}.tar.gz
Patch0:         bzr-gtk-disable-notifier.patch
Patch1:         bzr-gtk-0.94-setup-trailling-newline.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  python-devel bzr
BuildRequires:  gettext
Requires:       bzr >= 1.0
Requires:       pygtk2.0
Requires:       pygtk2.0-libglade
# These enable the commit-notify and nautilus browse functionality resp.  But
# neither are packaged for Mandriva yet.
#Requires:       bzr-dbus
#Requires:       python-nautilus

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

%prep
%setup -q
%patch0 -p1 -b .disable
%patch1 -p0 -b .newline

%build
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --skip-build --root $RPM_BUILD_ROOT
# as we don't support dbus extension yet
rm -f %{buildroot}/%{_datadir}/applications/bzr-notify.desktop
# mv $RPM_BUILD_ROOT%{python_sitelib}/bzrlib/plugins/gtk/nautilus* $RPM_BUILD_ROOT%{_prefix}/lib/nautilus/extensions-1.0/python/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README
%py_puresitedir/bzrlib/plugins/gtk/
%py_puresitedir/*egg-info
%{_datadir}/applications/bazaar-properties.desktop
%{_datadir}/applications/bzr-handle-patch.desktop
%{_datadir}/application-registry/bzr-gtk.applications
%{_datadir}/%{name}
%{_datadir}/pixmaps/bzr-icon-64.png
%{_iconsdir}/hicolor/scalable/emblems/*
%{_libdir}/nautilus/extensions-2.0/python/nautilus-bzr.py

%files -n olive
%defattr(-,root,root,-)
%{_bindir}/*
%py_puresitedir/bzrlib/plugins/gtk/olive
%{_datadir}/olive
%{_datadir}/pixmaps/olive-gtk.png
%{_datadir}/applications/olive-gtk.desktop
%{_datadir}/locale/*

#%files nautilus
#%{_prefix}/lib/nautilus/extensions-1.0/python/*
