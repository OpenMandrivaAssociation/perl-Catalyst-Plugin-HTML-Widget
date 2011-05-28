%define upstream_name    Catalyst-Plugin-HTML-Widget
%define upstream_version 1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	HTML Widget And Validation Framework
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Catalyst) >= 5.500.0
BuildRequires:	perl(HTML::Widget)

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{version}-%{release}-%{release}

%description
HTML Widget And Validation Framework

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst
