source <- "./inst/testme"
if (!utils::file_test("-d", source)) {
  stop("Source 'testme' folder not found: ", sQuote(source))
}

target <- "./tests"
if (!utils::file_test("-d", target)) {
  stop("Target 'tests' folder not found: ", sQuote(target))
}

r_path <- "./R"
if (!utils::file_test("-d", r_path)) {
  stop("Target 'R' folder not found: ", sQuote(r_path))
}

desc <- "./DESCRIPTION"
if (!utils::file_test("-f", desc)) {
  stop("'DESCRIPTION' file not found: ", sQuote(desc))
}
pkgname <- read.dcf(desc)[, "Package"]
if (is.na(pkgname) || !nzchar(pkgname)) {
  stop("Failed to infer package name from 'DESCRIPTION' file: ", sQuote(pkgname))
} else if (!requireNamespace(pkgname)) {
  stop("Package fail to load: ", sQuote(pkgname))
}


files <- dir(path = source, pattern = "^test-.*[.]R$", full.names = TRUE)
message(sprintf("Deploying %d test scripts ...", length(files)))

## Generate R unit test script
code <- c(
  "## This runs 'testme' test inst/testme/test-<name>.R scripts",
  "## Don't edit - it was autogenerated by inst/testme/deploy.R",
  "testme <- function(name) {",
  sprintf("  path <- system.file(package = '%s', 'testme', mustWork = TRUE)", pkgname),
  "  Sys.setenv(R_TESTME_PATH = path)",
  sprintf("  Sys.setenv(R_TESTME_PACKAGE = '%s')", pkgname),
  "  Sys.setenv(R_TESTME_NAME = name)",
  "  on.exit(Sys.unsetenv('R_TESTME_NAME'))",
  "  source(file.path(path, 'run.R'))",
  "}"
)
writeLines(code, con = file.path("./R/testme.R"))

for (kk in seq_along(files)) {
  file <- files[kk]

  source_file <- basename(file)
  name <- sub("^test-", "", sub("[.]R$", "", source_file))
  target_file <- file.path(target, source_file)
  
  message(sprintf("%02d/%02d test script %s", kk, length(files), sQuote(target_file)))

  ## Assert that testme script can be parsed
  res <- tryCatch(parse(file = file), error = identity)
  if (inherits(res, "error")) {
    stop("Syntax error: ", sQuote(file))
  }

  ## Generate R unit test script
  code <- c(
    sprintf("## This runs testme test script inst/testme/test-%s.R", name),
    "## Don't edit - it was autogenerated by inst/testme/deploy.R",
    sprintf('%s:::testme("%s")', pkgname, name)
  )
  writeLines(code, con = target_file)
}

message(sprintf("Deploying %d test scripts ... done", length(files)))
