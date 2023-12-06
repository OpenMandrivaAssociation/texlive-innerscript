Name:		texlive-innerscript
Version:	68776
Release:	1
Summary:	Modifies automatic mathematics spacing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/innerscript
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/innerscript.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/innerscript.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/innerscript.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package modifies two aspects of TeX's automatic interatom
mathematics spacing. It uses LuaTeX's \Umath primitives to make
superscripts and subscripts more closely resemble \textstyle
and \displaystyle math and to treat \mathinner subformulas as
\mathord, effectively eliminating this class.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/innerscript
%{_texmfdistdir}/tex/lualatex/innerscript
%doc %{_texmfdistdir}/doc/lualatex/innerscript

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
