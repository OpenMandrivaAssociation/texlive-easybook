Name:		texlive-easybook
Version:	72211
Release:	1
Summary:	Easily typesetting Chinese theses or books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easybook
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easybook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easybook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easybook.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
easybook is a pure academic template created based on the
ctexbook book document class. It also has the functions of book
and article document class. Combined with the general framework
design of the dissertation of many universities in China,
providing multiple commands and interfaces allows users to
easily customize the thesis template. Its basic macro package
easybase can also be used with CTeX and standard document
classes.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/easybook
%{_texmfdistdir}/tex/latex/easybook
%doc %{_texmfdistdir}/doc/latex/easybook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
