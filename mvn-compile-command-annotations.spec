#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-compile-command-annotations
Version  : 1.2.0
Release  : 3
URL      : https://github.com/nicoulaj/compile-command-annotations/archive/1.2.0.tar.gz
Source0  : https://github.com/nicoulaj/compile-command-annotations/archive/1.2.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0-sources.jar
Source2  : https://repo.maven.apache.org/maven2/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0.jar
Source3  : https://repo.maven.apache.org/maven2/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-compile-command-annotations-data = %{version}-%{release}
Requires: mvn-compile-command-annotations-license = %{version}-%{release}

%description
compile-command-annotations [![Build Status](https://travis-ci.org/nicoulaj/compile-command-annotations.svg)](https://travis-ci.org/nicoulaj/compile-command-annotations)
=====================

%package data
Summary: data components for the mvn-compile-command-annotations package.
Group: Data

%description data
data components for the mvn-compile-command-annotations package.


%package license
Summary: license components for the mvn-compile-command-annotations package.
Group: Default

%description license
license components for the mvn-compile-command-annotations package.


%prep
%setup -q -n compile-command-annotations-1.2.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-compile-command-annotations
cp COPYING %{buildroot}/usr/share/package-licenses/mvn-compile-command-annotations/COPYING
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0-sources.jar
/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0.jar
/usr/share/java/.m2/repository/net/ju-n/compile-command-annotations/compile-command-annotations/1.2.0/compile-command-annotations-1.2.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-compile-command-annotations/COPYING
