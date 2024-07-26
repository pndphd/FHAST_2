#-----------------------------------------------------------------------------
# HDF4 Version file for install directory
#-----------------------------------------------------------------------------
#
# The created file sets PACKAGE_VERSION_EXACT if the current version string and
# the requested version string are exactly the same and it sets
# PACKAGE_VERSION_COMPATIBLE if the current version is >= requested version,
# but only if the requested major.minor version is the same as the current one.
# The variable HDF4_VERSION_STRING must be set before calling configure_file().

set (PACKAGE_VERSION "4.2.14")

if("${PACKAGE_VERSION}" VERSION_LESS "${PACKAGE_FIND_VERSION}" )
  set(PACKAGE_VERSION_COMPATIBLE FALSE)
else()
  if ("${PACKAGE_FIND_VERSION_MAJOR}" STREQUAL "4")

    # exact match for version .2
    if ("${PACKAGE_FIND_VERSION_MINOR}" STREQUAL "2")

      # compatible with any version 4.2.x
      set (PACKAGE_VERSION_COMPATIBLE TRUE)

      if ("${PACKAGE_FIND_VERSION_PATCH}" STREQUAL "14")
        set (PACKAGE_VERSION_EXACT TRUE)

        if ("${PACKAGE_FIND_VERSION_TWEAK}" STREQUAL "")
          # not using this yet
        endif ()
      endif ()
    else ()
      set (PACKAGE_VERSION_COMPATIBLE FALSE)
    endif ()
  endif ()
endif()

# if the installed or the using project don't have CMAKE_SIZEOF_VOID_P set, ignore it:
if("${CMAKE_SIZEOF_VOID_P}"  STREQUAL ""  OR "8" STREQUAL "")
   return()
endif()

# check that the installed version has the same 32/64bit-ness as the one which is currently searching:
if(NOT "${CMAKE_SIZEOF_VOID_P}" STREQUAL "8")
  math(EXPR installedBits "8 * 8")
  set(PACKAGE_VERSION "${PACKAGE_VERSION} (${installedBits}bit)")
  set(PACKAGE_VERSION_UNSUITABLE TRUE)
endif()
