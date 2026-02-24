srpm:
	$$(git --version) || dnf -y install git; \
	MISSING_DEPS=$$($(MAKE) -C redhat dist-get-buildreqs | grep "Missing dependencies:" | cut -d":" -f2-); \
	[ -n "$$MISSING_DEPS" ] && dnf -y install $$MISSING_DEPS; \
	$(MAKE) -C redhat dist-srpm DISTLOCALVERSION="" DIST="$$(rpm --eval %distcore)"; \
	[ -n "$(outdir)" ] && mv redhat/rpm/SRPMS/*.src.rpm $(outdir); \
	true
