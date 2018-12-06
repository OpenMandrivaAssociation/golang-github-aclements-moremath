# Run tests in check section
# Tests are failing, disabled.
# Maybe related to https://github.com/aclements/go-moremath/issues/2
%bcond_with check

%global goipath         github.com/aclements/go-moremath
%global commit          b1aff36309c727972dd8b46fcc93f88763a62348

%global common_description %{expand:
These packages provide more specialized math routines than are available in 
the standard Go math package. go-moremath currently focuses on statistical 
routines, with particular focus on high-quality implementations and APIs 
for non-parametric methods.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        An assortment of more specialized math routines for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/gonum/matrix/mat64)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitb1aff36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180421gitb1aff36
- First package for Fedora

