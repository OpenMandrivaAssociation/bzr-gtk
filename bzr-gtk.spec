# based on http://cvs.fedora.redhat.com/viewcvs/devel/bzr-gtk/?root=extras
Name:           bzr-gtk
Version:        0.104.0
Release:        4
Summary:        Bazaar plugin for GTK+ interfaces to most Bazaar operations

Group:          Development/Python
License:        GPL
URL:            https://bazaar-vcs.org/bzr-gtk
Source0:	http://edge.launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel bzr
BuildRequires:  gettext
Requires:       bzr >= 2.1
Requires:	typelib(GtkSource) = 3.0
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(PangoCairo) = 1.0
%description
bzr-gtk is a plugin for Bazaar that aims to provide GTK+ interfaces to most
Bazaar operations.

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
python2 setup.py build


%install
touch credits.pickle
python2 setup.py install --root %{buildroot}
mkdir -p %{buildroot}%{_prefix}/lib/nautilus/extensions-1.0/python/
mv %{buildroot}%{python2_sitelib}/bzrlib/plugins/gtk/nautilus* %{buildroot}%{_prefix}/lib/nautilus/extensions-1.0/python/

%files
%doc COPYING README
%py2_puresitedir/bzrlib/plugins/gtk/
%py2_puresitedir/*egg-info
%{_bindir}/bzr-handle-patch
%{_bindir}/bzr-notify
%{_datadir}/applications/bazaar-properties.desktop
%{_datadir}/applications/bzr-handle-patch.desktop
%{_datadir}/applications/bzr-notify.desktop
%{_datadir}/application-registry/bzr-gtk.applications
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/bzr-panel.svg
%{_datadir}/pixmaps/bzr-icon-64.png
%{_iconsdir}/hicolor/scalable/emblems/*

%files nautilus
%{_prefix}/lib/nautilus/extensions-1.0/python/*


%changelog
* Fri Apr 13 2012 Crispin Boylan <crisb@mandriva.org> 0.104.0-1mdv2012.0
+ Revision: 790507
- New release

* Tue Feb 28 2012 Crispin Boylan <crisb@mandriva.org> 0.103.0-1
+ Revision: 781254
- New release

* Fri Mar 18 2011 Crispin Boylan <crisb@mandriva.org> 0.100.0-1
+ Revision: 646332
- New release

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0.99.0-4mdv2011.0
+ Revision: 598901
- rebuild

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.99.0-3mdv2011.0
+ Revision: 592420
- rebuild for python 2.7

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.99.0-2mdv2011.0
+ Revision: 591767
- Rebuild

* Mon Sep 13 2010 Crispin Boylan <crisb@mandriva.org> 0.99.0-1mdv2011.0
+ Revision: 578089
- New release, splits off olive into a separate package

* Sun Aug 08 2010 Crispin Boylan <crisb@mandriva.org> 0.98.0-2mdv2011.0
+ Revision: 567638
- Patch 1
- Compatible with bzr 2.2 (patch1)

* Fri Mar 05 2010 Crispin Boylan <crisb@mandriva.org> 0.98.0-1mdv2010.1
+ Revision: 514793
- New release, drop patch0 (merged)

* Tue Feb 23 2010 Crispin Boylan <crisb@mandriva.org> 0.97.0-2mdv2010.1
+ Revision: 510374
- Add patch file
- Patch 0 - mark as compatible with bzr 2.1

* Sun Aug 30 2009 Crispin Boylan <crisb@mandriva.org> 0.97.0-1mdv2010.0
+ Revision: 422470
- New release

* Mon Jul 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.96.2-1mdv2010.0
+ Revision: 398124
- Update to new version 0.96.2

* Fri Dec 26 2008 Crispin Boylan <crisb@mandriva.org> 0.95.0-2mdv2009.1
+ Revision: 319438
- Rebuild for python2.6

* Sat Nov 08 2008 Crispin Boylan <crisb@mandriva.org> 0.95.0-1mdv2009.1
+ Revision: 300991
- New version
- Remove obsolete patches
- Enable Nautilus integration

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - added requires to newer bzr and pygtk2.0-libglade
    - new version 0.94.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 14 2007 Jérôme Soyer <saispo@mandriva.org> 0.93.0-1mdv2008.1
+ Revision: 119744
- New release 0.93.0

* Wed Nov 14 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.92.1-1mdv2008.1
+ Revision: 108868
- new version 0.92.1

* Fri Oct 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.91.0-1mdv2008.1
+ Revision: 97327
- New release 0.91.0

* Mon Sep 03 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.90.0-1mdv2008.0
+ Revision: 78575
- new version 0.90.0

* Tue Jul 17 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.18.0-1mdv2008.0
+ Revision: 52933
- changed group name to Development/Other
- new version 0.18.0

* Mon Jun 18 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.17.0-1mdv2008.0
+ Revision: 41049
- requires new bzr 0.17
- don't rely on __id_u
- new version 0.17.0

* Sat May 26 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.16.0-1mdv2008.0
+ Revision: 31234
- Import bzr-gtk

