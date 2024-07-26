#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "hdf4::xdr-static" for configuration "Release"
set_property(TARGET hdf4::xdr-static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(hdf4::xdr-static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libxdr.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS hdf4::xdr-static )
list(APPEND _IMPORT_CHECK_FILES_FOR_hdf4::xdr-static "${_IMPORT_PREFIX}/lib/libxdr.lib" )

# Import target "hdf4::hdf-static" for configuration "Release"
set_property(TARGET hdf4::hdf-static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(hdf4::hdf-static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libhdf.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS hdf4::hdf-static )
list(APPEND _IMPORT_CHECK_FILES_FOR_hdf4::hdf-static "${_IMPORT_PREFIX}/lib/libhdf.lib" )

# Import target "hdf4::mfhdf-static" for configuration "Release"
set_property(TARGET hdf4::mfhdf-static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(hdf4::mfhdf-static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libmfhdf.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS hdf4::mfhdf-static )
list(APPEND _IMPORT_CHECK_FILES_FOR_hdf4::mfhdf-static "${_IMPORT_PREFIX}/lib/libmfhdf.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
