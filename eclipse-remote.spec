%{?scl:%scl_package eclipse-remote}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global git_tag R2_0

Name:           %{?scl_prefix}eclipse-remote
Version:        2.0.0
Release:        1.2.bs2%{?dist}
Summary:        Eclipse Remote Services plug-in
License:        EPL
URL:            https://www.eclipse.org/ptp/

Source0:        http://git.eclipse.org/c/ptp/org.eclipse.remote.git/snapshot/%{git_tag}.tar.xz

BuildArch:      noarch

BuildRequires:    %{?scl_prefix}tycho
BuildRequires:    %{?scl_prefix}tycho-extras
BuildRequires:    %{?scl_prefix_java_common}jsch
BuildRequires:    %{?scl_prefix}eclipse-pde >= 1:4.3.2
BuildRequires:    %{?scl_prefix}eclipse-license
BuildRequires:    %{?scl_prefix}eclipse-cdt
BuildRequires:    %{?scl_prefix}eclipse-tm-terminal

Requires:         %{?scl_prefix_java_common}jsch
Requires:         %{?scl_prefix}eclipse-platform >= 1:4.3.2

%description
Remote Services provides an extensible remote services framework.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n %{git_tag}

find -name *.jar -exec rm -rf {} \;
find -name *.class -exec rm -rf {} \;

%pom_remove_plugin org.eclipse.tycho:tycho-packaging-plugin releng/org.eclipse.remote.build/pom.xml

%pom_disable_module ../../releng/org.eclipse.remote.repo releng/org.eclipse.remote.build/pom.xml

# Don't package parent pom
%mvn_package org.eclipse.remote:remote-parent __noinstall
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build  -j -- -f releng/org.eclipse.remote.build/pom.xml
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc features/org.eclipse.remote-feature/epl-v10.html

%changelog
* Thu Jul 16 2015 Mat Booth <mat.booth@redhat.com> - 2.0.0-1.2
- Fix unowned directories

* Thu Jul 16 2015 Mat Booth <mat.booth@redhat.com> - 2.0.0-1.1
- Import latest from Fedora

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Update to 2.0 final.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.4.git4488f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 3 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-0.3.git4488f6f
- BR eclipse-tm-terminal to do full build.

* Tue Jun 2 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-0.2.git4488f6f
- New git snapshot.
- Build serial plugins.

* Mon Jun 1 2015 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-0.1.git76ac23a
- Update to 2.0 prerelease.

* Wed Mar 04 2015 Mat Booth <mat.booth@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Fri Feb  6 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-2
- Rebuild to generate missing OSGi auto-requires

* Tue Sep 30 2014 Mat Booth <mat.booth@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Sep 25 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-3
- Rebuild to regenerate auto requires

* Fri Sep 12 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Build/install with xmvn

* Fri Jun 27 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Update to upstream released version
- Add BR on eclipse-license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.git19f4d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.4.git19f4d9
- Drop requirement on jpackage-utils

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.3.git19f4d9
- Update to latest upstream.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.2.gite09793
- Don't include the cdt feature.

* Tue May 06 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-0.1.gite09793
- Initial package.
