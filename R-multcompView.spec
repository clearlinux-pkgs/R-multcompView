#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-multcompView
Version  : 0.1.9
Release  : 45
URL      : https://cran.r-project.org/src/contrib/multcompView_0.1-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/multcompView_0.1-9.tar.gz
Summary  : Visualizations of Paired Comparisons
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
p-values or a correlation, difference, or distance
    matrix into a display identifying the pairs for
    which the differences were not significantly
    different.  Designed for use in conjunction with
    the output of functions like TukeyHSD, dist{stats},
    simint, simtest, csimint, csimtest{multcomp},
    friedmanmc, kruskalmc{pgirmess}.

%prep
%setup -q -n multcompView

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681138605

%install
export SOURCE_DATE_EPOCH=1681138605
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/multcompView/DESCRIPTION
/usr/lib64/R/library/multcompView/INDEX
/usr/lib64/R/library/multcompView/Meta/Rd.rds
/usr/lib64/R/library/multcompView/Meta/features.rds
/usr/lib64/R/library/multcompView/Meta/hsearch.rds
/usr/lib64/R/library/multcompView/Meta/links.rds
/usr/lib64/R/library/multcompView/Meta/nsInfo.rds
/usr/lib64/R/library/multcompView/Meta/package.rds
/usr/lib64/R/library/multcompView/NAMESPACE
/usr/lib64/R/library/multcompView/R/multcompView
/usr/lib64/R/library/multcompView/R/multcompView.rdb
/usr/lib64/R/library/multcompView/R/multcompView.rdx
/usr/lib64/R/library/multcompView/help/AnIndex
/usr/lib64/R/library/multcompView/help/aliases.rds
/usr/lib64/R/library/multcompView/help/multcompView.rdb
/usr/lib64/R/library/multcompView/help/multcompView.rdx
/usr/lib64/R/library/multcompView/help/paths.rds
/usr/lib64/R/library/multcompView/html/00Index.html
/usr/lib64/R/library/multcompView/html/R.css
