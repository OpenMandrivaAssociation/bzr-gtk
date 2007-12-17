# based on http://cvs.fedora.redhat.com/viewcvs/devel/bzr-gtk/?root=extras
Name:           bzr-gtk
Version:        0.93.0
Release:        %mkrel 1
Summary:        Bazaar plugin for GTK+ interfaces to most Bazaar operations

Group:          Development/Python
License:        GPL
URL:            http://bazaar-vcs.org/bzr-gtk
Source0:        http://samba.org/~jelmer/bzr/bzr-gtk-%{version}.tar.gz
Patch0:         bzr-gtk-disable-notifier.patch

BuildArch:      noarch
BuildRequires:  python-devel bzr
BuildRequires:  gettext
Requires:       bzr >= 0.17 pygtk2.0
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
%patch -p1 -b .disable

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

%files -n olive
%defattr(-,root,root,-)
%{_bindir}/*
%py_puresitedir/olive
%{_datadir}/olive/
%{_datadir}/pixmaps/olive-gtk.png
%{_datadir}/applications/olive-gtk.desktop

#%files nautilus
#%{_prefix}/lib/nautilus/extensions-1.0/python/*
