%{?scl:%scl_package eclipse-remote}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global git_tag R1_1_1

Name:           %{?scl_prefix}eclipse-remote
Version:        1.1.1
Release:        1.bootstrap1%{?dist}
Summary:        Eclipse Remote Services plug-in
License:        EPL
URL:            https://www.eclipse.org/ptp/

Source0:        http://git.eclipse.org/c/ptp/org.eclipse.remote.git/snapshot/org.eclipse.remote-%{git_tag}.tar.bz2

BuildArch:      noarch

BuildRequires:    %{?scl_prefix}tycho
BuildRequires:    %{?scl_prefix}tycho-extras
BuildRequires:    %{?scl_prefix_java_common}jsch
BuildRequires:    %{?scl_prefix}eclipse-pde >= 1:4.3.2
BuildRequires:    %{?scl_prefix}eclipse-license

Requires:         %{?scl_prefix_java_common}jsch
Requires:         %{?scl_prefix}eclipse-platform >= 1:4.3.2

%description
Remote Services provides an extensible remote services framework.

%prep
%setup -q -n org.eclipse.remote-%{git_tag}

find -name *.jar -exec rm -rf {} \;
find -name *.class -exec rm -rf {} \;

%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl_maven} %{scl} - <<"EOF"}
%pom_remove_plugin org.eclipse.tycho:tycho-packaging-plugin releng/org.eclipse.remote.build/pom.xml
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl_maven} %{scl} - <<"EOF"}
%mvn_build  -j -- -f releng/org.eclipse.remote.build/pom.xml
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl_maven} %{scl} - <<"EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc features/org.eclipse.remote-feature/epl-v10.html

%changelog
* Wed Mar 04 2015 Mat Booth <mat.booth@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Tue Jan 13 2015 Mat Booth <mat.booth@redhat.com> - 1.1.0-1.2
- Related: rhbz#1175105 - Regenerate auto-provides

* Tue Jan 13 2015 Mat Booth <mat.booth@redhat.com> - 1.1.0-1.1
- Related: rhbz#1175105 - Import into DTS 3.1

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
