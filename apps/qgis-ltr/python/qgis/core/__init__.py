# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : May 2014
    Copyright            : (C) 2014 by Nathan Woodrow
    Email                : woodrow dot nathan at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nathan Woodrow'
__date__ = 'May 2014'
__copyright__ = '(C) 2014, Nathan Woodrow'

from qgis.PyQt.QtCore import NULL
from qgis._core import *

from .additions.edit import edit, QgsEditError
from .additions.fromfunction import fromFunction
from .additions.metaenum import metaEnumFromType, metaEnumFromValue
from .additions.processing import processing_output_layer_repr, processing_source_repr
from .additions.projectdirtyblocker import ProjectDirtyBlocker
from .additions.providermetadata import PyProviderMetadata
from .additions.qgsfeature import mapping_feature
from .additions.qgsfunction import register_function, qgsfunction
from .additions.qgsgeometry import _geometryNonZero, mapping_geometry
from .additions.qgssettings import _qgssettings_enum_value, _qgssettings_set_enum_value, _qgssettings_flag_value
from .additions.qgstaskwrapper import QgsTaskWrapper
from .additions.readwritecontextentercategory import ReadWriteContextEnterCategory
from .additions.runtimeprofiler import ScopedRuntimeProfileContextManager
from .additions.validitycheck import check

# Injections into classes
QgsFeature.__geo_interface__ = property(mapping_feature)
QgsGeometry.__bool__ = _geometryNonZero
QgsGeometry.__geo_interface__ = property(mapping_geometry)
QgsGeometry.__nonzero__ = _geometryNonZero
QgsProcessingFeatureSourceDefinition.__repr__ = processing_source_repr
QgsProcessingOutputLayerDefinition.__repr__ = processing_output_layer_repr
QgsProject.blockDirtying = ProjectDirtyBlocker
QgsReadWriteContext.enterCategory = ReadWriteContextEnterCategory
QgsRuntimeProfiler.profile = ScopedRuntimeProfileContextManager
QgsSettings.enumValue = _qgssettings_enum_value
QgsSettings.setEnumValue = _qgssettings_set_enum_value
QgsSettings.flagValue = _qgssettings_flag_value
QgsTask.fromFunction = fromFunction

# Classes patched using a derived class
QgsProviderMetadata = PyProviderMetadata

# monkey patch deprecated enum values to maintain API
# TODO - remove for QGIS 4.0
QgsMarkerLineSymbolLayer.Interval = QgsTemplatedLineSymbolLayerBase.Interval
QgsMarkerLineSymbolLayer.Vertex = QgsTemplatedLineSymbolLayerBase.Vertex
QgsMarkerLineSymbolLayer.LastVertex = QgsTemplatedLineSymbolLayerBase.LastVertex
QgsMarkerLineSymbolLayer.FirstVertex = QgsTemplatedLineSymbolLayerBase.FirstVertex
QgsMarkerLineSymbolLayer.CentralPoint = QgsTemplatedLineSymbolLayerBase.CentralPoint
QgsMarkerLineSymbolLayer.CurvePoint = QgsTemplatedLineSymbolLayerBase.CurvePoint

# Monkey patch static const "QgsDataProvider.SUBLAYER_SEPARATOR" which was removed for QGIS 3.12
QgsDataProvider.SUBLAYER_SEPARATOR = QgsDataProvider.sublayerSeparator()

# Monkey patch Qgis vars
Qgis.QGIS_VERSION = Qgis.version()
Qgis.QGIS_VERSION_INT = Qgis.versionInt()
Qgis.QGIS_RELEASE_NAME = Qgis.releaseName()

GEOWKT = geoWkt()
PROJECT_SCALES = Qgis.defaultProjectScales()
GEOPROJ4 = geoProj4()
GEO_EPSG_CRS_AUTHID = geoEpsgCrsAuthId()
GEO_NONE = geoNone()
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/core/qgis.h
Qgis.DataType.baseClass = Qgis
Qgis.PythonMacroMode.baseClass = Qgis
# The following has been generated automatically from src/core/qgsabstractdatabaseproviderconnection.h
QgsAbstractDatabaseProviderConnection.TableFlags.baseClass = QgsAbstractDatabaseProviderConnection
TableFlags = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
QgsAbstractDatabaseProviderConnection.Capability.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.Capabilities.baseClass = QgsAbstractDatabaseProviderConnection
Capabilities = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
QgsAbstractDatabaseProviderConnection.GeometryColumnCapability.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.GeometryColumnCapabilities.baseClass = QgsAbstractDatabaseProviderConnection
GeometryColumnCapabilities = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/geometry/qgsabstractgeometry.h
QgsAbstractGeometry.SegmentationToleranceType.baseClass = QgsAbstractGeometry
# The following has been generated automatically from src/core/qgsattributeeditorelement.h
QgsAttributeEditorRelation.Button.baseClass = QgsAttributeEditorRelation
QgsAttributeEditorRelation.Buttons.baseClass = QgsAttributeEditorRelation
Buttons = QgsAttributeEditorRelation  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/auth/qgsauthmanager.h
QgsAuthManager.MessageLevel.baseClass = QgsAuthManager
# The following has been generated automatically from src/core/qgsdataitem.h
QgsDataItem.Type.baseClass = QgsDataItem
QgsDataItem.State.baseClass = QgsDataItem
QgsLayerItem.LayerType.baseClass = QgsLayerItem
# The following has been generated automatically from src/core/qgsdatasourceuri.h
QgsDataSourceUri.SslMode.baseClass = QgsDataSourceUri
# The following has been generated automatically from src/core/qgsdefaultvalue.h
QgsDefaultValue.__bool__ = lambda self: self.isValid()
# The following has been generated automatically from src/core/dxf/qgsdxfexport.h
# monkey patching scoped based enum
QgsDxfExport.ExportResult.Success.__doc__ = "Successful export"
QgsDxfExport.ExportResult.InvalidDeviceError.__doc__ = "Invalid device error"
QgsDxfExport.ExportResult.DeviceNotWritableError.__doc__ = "Device not writable error"
QgsDxfExport.ExportResult.EmptyExtentError.__doc__ = "Empty extent, no extent given and no extent could be derived from layers"
QgsDxfExport.ExportResult.__doc__ = 'The result of an export as dxf operation\n\n.. versionadded:: 3.10.1\n\n' + '* ``Success``: ' + QgsDxfExport.ExportResult.Success.__doc__ + '\n' + '* ``InvalidDeviceError``: ' + QgsDxfExport.ExportResult.InvalidDeviceError.__doc__ + '\n' + '* ``DeviceNotWritableError``: ' + QgsDxfExport.ExportResult.DeviceNotWritableError.__doc__ + '\n' + '* ``EmptyExtentError``: ' + QgsDxfExport.ExportResult.EmptyExtentError.__doc__
# --
# monkey patching scoped based enum
QgsDxfExport.VAlign.VBaseLine.__doc__ = "Top (0)"
QgsDxfExport.VAlign.VBottom.__doc__ = "Bottom (1)"
QgsDxfExport.VAlign.VMiddle.__doc__ = "Middle (2)"
QgsDxfExport.VAlign.VTop.__doc__ = "Top (3)"
QgsDxfExport.VAlign.Undefined.__doc__ = "Undefined"
QgsDxfExport.VAlign.__doc__ = 'Vertical alignments.\n\n' + '* ``VBaseLine``: ' + QgsDxfExport.VAlign.VBaseLine.__doc__ + '\n' + '* ``VBottom``: ' + QgsDxfExport.VAlign.VBottom.__doc__ + '\n' + '* ``VMiddle``: ' + QgsDxfExport.VAlign.VMiddle.__doc__ + '\n' + '* ``VTop``: ' + QgsDxfExport.VAlign.VTop.__doc__ + '\n' + '* ``Undefined``: ' + QgsDxfExport.VAlign.Undefined.__doc__
# --
# monkey patching scoped based enum
QgsDxfExport.HAlign.HLeft.__doc__ = "Left (0)"
QgsDxfExport.HAlign.HCenter.__doc__ = "Centered (1)"
QgsDxfExport.HAlign.HRight.__doc__ = "Right (2)"
QgsDxfExport.HAlign.HAligned.__doc__ = "Aligned = (3) (if VAlign==0)"
QgsDxfExport.HAlign.HMiddle.__doc__ = "Middle = (4) (if VAlign==0)"
QgsDxfExport.HAlign.HFit.__doc__ = "Fit into point = (5) (if VAlign==0)"
QgsDxfExport.HAlign.Undefined.__doc__ = "Undefined"
QgsDxfExport.HAlign.__doc__ = 'Horizontal alignments.\n\n' + '* ``HLeft``: ' + QgsDxfExport.HAlign.HLeft.__doc__ + '\n' + '* ``HCenter``: ' + QgsDxfExport.HAlign.HCenter.__doc__ + '\n' + '* ``HRight``: ' + QgsDxfExport.HAlign.HRight.__doc__ + '\n' + '* ``HAligned``: ' + QgsDxfExport.HAlign.HAligned.__doc__ + '\n' + '* ``HMiddle``: ' + QgsDxfExport.HAlign.HMiddle.__doc__ + '\n' + '* ``HFit``: ' + QgsDxfExport.HAlign.HFit.__doc__ + '\n' + '* ``Undefined``: ' + QgsDxfExport.HAlign.Undefined.__doc__
# --
# The following has been generated automatically from src/core/qgseditformconfig.h
QgsEditFormConfig.EditorLayout.baseClass = QgsEditFormConfig
QgsEditFormConfig.FeatureFormSuppress.baseClass = QgsEditFormConfig
QgsEditFormConfig.PythonInitCodeSource.baseClass = QgsEditFormConfig
# The following has been generated automatically from src/core/qgsfieldproxymodel.h
QgsFieldProxyModel.Filters.baseClass = QgsFieldProxyModel
Filters = QgsFieldProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/geometry/qgsgeometry.h
QgsGeometry.OperationResult.baseClass = QgsGeometry
QgsGeometry.BufferSide.baseClass = QgsGeometry
QgsGeometry.EndCapStyle.baseClass = QgsGeometry
QgsGeometry.JoinStyle.baseClass = QgsGeometry
# The following has been generated automatically from src/core/geocms/geonode/qgsgeonoderequest.h
# monkey patching scoped based enum
QgsGeoNodeRequest.BackendServer.Unknown.__doc__ = "Unknown backend"
QgsGeoNodeRequest.BackendServer.QgisServer.__doc__ = "QGIS server used as backend"
QgsGeoNodeRequest.BackendServer.Geoserver.__doc__ = "Geoserver used as backend"
QgsGeoNodeRequest.BackendServer.__doc__ = 'GeoNode backend server type.\n\n' + '* ``Unknown``: ' + QgsGeoNodeRequest.BackendServer.Unknown.__doc__ + '\n' + '* ``QgisServer``: ' + QgsGeoNodeRequest.BackendServer.QgisServer.__doc__ + '\n' + '* ``Geoserver``: ' + QgsGeoNodeRequest.BackendServer.Geoserver.__doc__
# --
# The following has been generated automatically from src/core/labeling/qgslabellinesettings.h
# monkey patching scoped based enum
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolLeftRight.__doc__ = "Place direction symbols on left/right of label"
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolAbove.__doc__ = "Place direction symbols on above label"
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolBelow.__doc__ = "Place direction symbols on below label"
QgsLabelLineSettings.DirectionSymbolPlacement.__doc__ = 'Placement options for direction symbols.\n\n' + '* ``SymbolLeftRight``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolLeftRight.__doc__ + '\n' + '* ``SymbolAbove``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolAbove.__doc__ + '\n' + '* ``SymbolBelow``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolBelow.__doc__
# --
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorType.HintOnly.__doc__ = "Line anchor is a hint for preferred placement only, but other placements close to the hint are permitted"
QgsLabelLineSettings.AnchorType.Strict.__doc__ = "Line anchor is a strict placement, and other placements are not permitted"
QgsLabelLineSettings.AnchorType.__doc__ = 'Line anchor types\n\n' + '* ``HintOnly``: ' + QgsLabelLineSettings.AnchorType.HintOnly.__doc__ + '\n' + '* ``Strict``: ' + QgsLabelLineSettings.AnchorType.Strict.__doc__
# --
# The following has been generated automatically from src/core/layout/qgslayoutmanager.h
QgsLayoutManagerProxyModel.Filters.baseClass = QgsLayoutManagerProxyModel
Filters = QgsLayoutManagerProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/locator/qgslocatorfilter.h
QgsLocatorFilter.Priority.baseClass = QgsLocatorFilter
QgsLocatorFilter.Flags.baseClass = QgsLocatorFilter
Flags = QgsLocatorFilter  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmapclippingregion.h
# monkey patching scoped based enum
QgsMapClippingRegion.FeatureClippingType.ClipToIntersection.__doc__ = "Clip the geometry of these features to the region prior to rendering (i.e. feature boundaries will follow the clip region)"
QgsMapClippingRegion.FeatureClippingType.ClipPainterOnly.__doc__ = "Applying clipping on the painter only (i.e. feature boundaries will be unchanged, but may be invisible where the feature falls outside the clipping region)"
QgsMapClippingRegion.FeatureClippingType.NoClipping.__doc__ = "Only render features which intersect the clipping region, but do not clip these features to the region"
QgsMapClippingRegion.FeatureClippingType.__doc__ = 'Feature clipping behavior, which controls how features from vector layers\nwill be clipped.\n\n' + '* ``ClipToIntersection``: ' + QgsMapClippingRegion.FeatureClippingType.ClipToIntersection.__doc__ + '\n' + '* ``ClipPainterOnly``: ' + QgsMapClippingRegion.FeatureClippingType.ClipPainterOnly.__doc__ + '\n' + '* ``NoClipping``: ' + QgsMapClippingRegion.FeatureClippingType.NoClipping.__doc__
# --
# The following has been generated automatically from src/core/qgsmaplayer.h
QgsMapLayer.LayerType = QgsMapLayerType
# monkey patching scoped based enum
QgsMapLayer.VectorLayer = QgsMapLayerType.VectorLayer
QgsMapLayer.VectorLayer.__doc__ = ""
QgsMapLayer.RasterLayer = QgsMapLayerType.RasterLayer
QgsMapLayer.RasterLayer.__doc__ = ""
QgsMapLayer.PluginLayer = QgsMapLayerType.PluginLayer
QgsMapLayer.PluginLayer.__doc__ = ""
QgsMapLayer.MeshLayer = QgsMapLayerType.MeshLayer
QgsMapLayer.MeshLayer.__doc__ = "Added in 3.2"
QgsMapLayer.VectorTileLayer = QgsMapLayerType.VectorTileLayer
QgsMapLayer.VectorTileLayer.__doc__ = "Added in 3.14"
QgsMapLayer.AnnotationLayer = QgsMapLayerType.AnnotationLayer
QgsMapLayer.AnnotationLayer.__doc__ = "Contains freeform, georeferenced annotations. Added in QGIS 3.16"
QgsMapLayerType.__doc__ = 'Types of layers that can be added to a map\n\n.. versionadded:: 3.8\n\n' + '* ``VectorLayer``: ' + QgsMapLayerType.VectorLayer.__doc__ + '\n' + '* ``RasterLayer``: ' + QgsMapLayerType.RasterLayer.__doc__ + '\n' + '* ``PluginLayer``: ' + QgsMapLayerType.PluginLayer.__doc__ + '\n' + '* ``MeshLayer``: ' + QgsMapLayerType.MeshLayer.__doc__ + '\n' + '* ``VectorTileLayer``: ' + QgsMapLayerType.VectorTileLayer.__doc__ + '\n' + '* ``AnnotationLayer``: ' + QgsMapLayerType.AnnotationLayer.__doc__
# --
QgsMapLayer.LayerFlag.baseClass = QgsMapLayer
QgsMapLayer.LayerFlags.baseClass = QgsMapLayer
LayerFlags = QgsMapLayer  # dirty hack since SIP seems to introduce the flags in module
QgsMapLayer.StyleCategory.baseClass = QgsMapLayer
QgsMapLayer.StyleCategories.baseClass = QgsMapLayer
StyleCategories = QgsMapLayer  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmaplayermodel.h
QgsMapLayerModel.ItemDataRole.baseClass = QgsMapLayerModel
# The following has been generated automatically from src/core/qgsmaplayerproxymodel.h
QgsMapLayerProxyModel.Filters.baseClass = QgsMapLayerProxyModel
Filters = QgsMapLayerProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmapsettingsutils.h
# monkey patching scoped based enum
QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__ = "Ignore advanced effects which are supported in GeoPDF exports"
QgsMapSettingsUtils.EffectsCheckFlag.__doc__ = 'Flags for controlling the behavior of :py:func:`~QgsMapSettingsUtils.containsAdvancedEffects`\n\n.. versionadded:: 3.14\n\n' + '* ``IgnoreGeoPdfSupportedEffects``: ' + QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__
# --
# The following has been generated automatically from src/core/qgsnetworkcontentfetcherregistry.h
QgsNetworkContentFetcherRegistry.FetchingMode.baseClass = QgsNetworkContentFetcherRegistry
# The following has been generated automatically from src/core/processing/qgsprocessingutils.h
# monkey patching scoped based enum
QgsProcessingUtils.UnknownType = QgsProcessingUtils.LayerHint.UnknownType
QgsProcessingUtils.LayerHint.UnknownType.__doc__ = "Unknown layer type"
QgsProcessingUtils.Vector = QgsProcessingUtils.LayerHint.Vector
QgsProcessingUtils.LayerHint.Vector.__doc__ = "Vector layer type"
QgsProcessingUtils.Raster = QgsProcessingUtils.LayerHint.Raster
QgsProcessingUtils.LayerHint.Raster.__doc__ = "Raster layer type"
QgsProcessingUtils.Mesh = QgsProcessingUtils.LayerHint.Mesh
QgsProcessingUtils.LayerHint.Mesh.__doc__ = "Mesh layer type, since QGIS 3.6"
QgsProcessingUtils.LayerHint.__doc__ = 'Layer type hints.\n\n.. versionadded:: 3.4\n\n' + '* ``UnknownType``: ' + QgsProcessingUtils.LayerHint.UnknownType.__doc__ + '\n' + '* ``Vector``: ' + QgsProcessingUtils.LayerHint.Vector.__doc__ + '\n' + '* ``Raster``: ' + QgsProcessingUtils.LayerHint.Raster.__doc__ + '\n' + '* ``Mesh``: ' + QgsProcessingUtils.LayerHint.Mesh.__doc__
# --
# The following has been generated automatically from src/core/qgsproject.h
# monkey patching scoped based enum
QgsProject.FlagDontResolveLayers = QgsProject.ReadFlag.FlagDontResolveLayers
QgsProject.ReadFlag.FlagDontResolveLayers.__doc__ = "Don't resolve layer paths (i.e. don't load any layer content). Dramatically improves project read time if the actual data from the layers is not required."
QgsProject.FlagDontLoadLayouts = QgsProject.ReadFlag.FlagDontLoadLayouts
QgsProject.ReadFlag.FlagDontLoadLayouts.__doc__ = "Don't load print layouts. Improves project read time if layouts are not required, and allows projects to be safely read in background threads (since print layouts are not thread safe)."
QgsProject.FlagTrustLayerMetadata = QgsProject.ReadFlag.FlagTrustLayerMetadata
QgsProject.ReadFlag.FlagTrustLayerMetadata.__doc__ = "Trust layer metadata. Improves project read time. Do not use it if layers' extent is not fixed during the project's use by QGIS and QGIS Server."
QgsProject.FlagDontStoreOriginalStyles = QgsProject.ReadFlag.FlagDontStoreOriginalStyles
QgsProject.ReadFlag.FlagDontStoreOriginalStyles.__doc__ = "Skip the initial XML style storage for layers. Useful for minimising project load times in non-interactive contexts."
QgsProject.ReadFlag.__doc__ = 'Flags which control project read behavior.\n\n.. versionadded:: 3.10\n\n' + '* ``FlagDontResolveLayers``: ' + QgsProject.ReadFlag.FlagDontResolveLayers.__doc__ + '\n' + '* ``FlagDontLoadLayouts``: ' + QgsProject.ReadFlag.FlagDontLoadLayouts.__doc__ + '\n' + '* ``FlagTrustLayerMetadata``: ' + QgsProject.ReadFlag.FlagTrustLayerMetadata.__doc__ + '\n' + '* ``FlagDontStoreOriginalStyles``: ' + QgsProject.ReadFlag.FlagDontStoreOriginalStyles.__doc__
# --
# monkey patching scoped based enum
QgsProject.FileFormat.Qgz.__doc__ = "Archive file format, supports auxiliary data"
QgsProject.FileFormat.Qgs.__doc__ = "Project saved in a clear text, does not support auxiliary data"
QgsProject.FileFormat.__doc__ = 'Flags which control project read behavior.\n\n.. versionadded:: 3.12\n\n' + '* ``Qgz``: ' + QgsProject.FileFormat.Qgz.__doc__ + '\n' + '* ``Qgs``: ' + QgsProject.FileFormat.Qgs.__doc__
# --
QgsProject.FileFormat.baseClass = QgsProject
# monkey patching scoped based enum
QgsProject.AvoidIntersectionsMode.AllowIntersections.__doc__ = "Overlap with any feature allowed when digitizing new features"
QgsProject.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer.__doc__ = "Overlap with features from the active layer when digitizing new features not allowed"
QgsProject.AvoidIntersectionsMode.AvoidIntersectionsLayers.__doc__ = "Overlap with features from a specified list of layers when digitizing new features not allowed"
QgsProject.AvoidIntersectionsMode.__doc__ = 'Flags which control how intersections of pre-existing feature are handled when digitizing new features.\n\n.. versionadded:: 3.14\n\n' + '* ``AllowIntersections``: ' + QgsProject.AvoidIntersectionsMode.AllowIntersections.__doc__ + '\n' + '* ``AvoidIntersectionsCurrentLayer``: ' + QgsProject.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer.__doc__ + '\n' + '* ``AvoidIntersectionsLayers``: ' + QgsProject.AvoidIntersectionsMode.AvoidIntersectionsLayers.__doc__
# --
QgsProject.AvoidIntersectionsMode.baseClass = QgsProject
# The following has been generated automatically from src/core/qgsproviderconnectionmodel.h
QgsProviderConnectionModel.Role.baseClass = QgsProviderConnectionModel
# The following has been generated automatically from src/core/qgsprovidermetadata.h
QgsMeshDriverMetadata.MeshDriverCapability.baseClass = QgsMeshDriverMetadata
QgsMeshDriverMetadata.MeshDriverCapabilities.baseClass = QgsMeshDriverMetadata
MeshDriverCapabilities = QgsMeshDriverMetadata  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
QgsProviderMetadata.FilterType.FilterVector.__doc__ = ""
QgsProviderMetadata.FilterType.FilterRaster.__doc__ = ""
QgsProviderMetadata.FilterType.FilterMesh.__doc__ = ""
QgsProviderMetadata.FilterType.FilterMeshDataset.__doc__ = ""
QgsProviderMetadata.FilterType.__doc__ = 'Type of file filters\n\n.. versionadded:: 3.10\n\n' + '* ``FilterVector``: ' + QgsProviderMetadata.FilterType.FilterVector.__doc__ + '\n' + '* ``FilterRaster``: ' + QgsProviderMetadata.FilterType.FilterRaster.__doc__ + '\n' + '* ``FilterMesh``: ' + QgsProviderMetadata.FilterType.FilterMesh.__doc__ + '\n' + '* ``FilterMeshDataset``: ' + QgsProviderMetadata.FilterType.FilterMeshDataset.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterdataprovider.h
# monkey patching scoped based enum
QgsRasterDataProvider.ResamplingMethod.Nearest.__doc__ = "Nearest-neighbour resamplikng"
QgsRasterDataProvider.ResamplingMethod.Bilinear.__doc__ = "Bilinear resamplikng"
QgsRasterDataProvider.ResamplingMethod.Cubic.__doc__ = "Bicubic resamplikng"
QgsRasterDataProvider.ResamplingMethod.__doc__ = 'Resampling method for provider-level resampling.\n\n.. versionadded:: 3.16\n\n' + '* ``Nearest``: ' + QgsRasterDataProvider.ResamplingMethod.Nearest.__doc__ + '\n' + '* ``Bilinear``: ' + QgsRasterDataProvider.ResamplingMethod.Bilinear.__doc__ + '\n' + '* ``Cubic``: ' + QgsRasterDataProvider.ResamplingMethod.Cubic.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterpipe.h
# monkey patching scoped based enum
QgsRasterPipe.ResamplingStage.ResampleFilter.__doc__ = ""
QgsRasterPipe.ResamplingStage.Provider.__doc__ = ""
QgsRasterPipe.ResamplingStage.__doc__ = 'Stage at which resampling occurs.\n\n.. versionadded:: 3.16\n\n' + '* ``ResampleFilter``: ' + QgsRasterPipe.ResamplingStage.ResampleFilter.__doc__ + '\n' + '* ``Provider``: ' + QgsRasterPipe.ResamplingStage.Provider.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterprojector.h
QgsRasterProjector.Precision.baseClass = QgsRasterProjector
# The following has been generated automatically from src/core/qgsrelation.h
QgsRelation.RelationStrength.baseClass = QgsRelation
# The following has been generated automatically from src/core/scalebar/qgsscalebarrenderer.h
# monkey patching scoped based enum
QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ = "Renderer utilizes the scalebar line symbol (see QgsScaleBarSettings::lineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ = "Renderer utilizes the scalebar fill symbol (see QgsScaleBarSettings::fillSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ = "Renderer utilizes the alternate scalebar fill symbol (see QgsScaleBarSettings::alternateFillSymbol() )"
QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ = "Renderer respects the QgsScaleBarSettings::units() setting"
QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ = "Renderer respects the QgsScaleBarSettings::mapUnitsPerScaleBarUnit() setting"
QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ = "Renderer uses the QgsScaleBarSettings::unitLabel() setting"
QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ = "Renderer uses the scalebar segments"
QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ = "Renderer uses the QgsScaleBarSettings::labelBarSpace() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings::labelVerticalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings::labelHorizontalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ = "Renderer uses the QgsScaleBarSettings::alignment() setting"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ = "Renderer uses the scalebar subdivisions (see QgsScaleBarSettings::numberOfSubdivisions() )"
QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ = "Renderer utilizes the scalebar division symbol (see QgsScaleBarSettings::divisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ = "Renderer utilizes the scalebar subdivision symbol (see QgsScaleBarSettings::subdivisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__ = "Renderer uses the scalebar subdivisions height (see QgsScaleBarSettings::subdivisionsHeight() )"
QgsScaleBarRenderer.Flag.__doc__ = 'Flags which control scalebar renderer behavior.\n\n.. versionadded:: 3.14\n\n' + '* ``FlagUsesLineSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ + '\n' + '* ``FlagUsesFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ + '\n' + '* ``FlagUsesAlternateFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ + '\n' + '* ``FlagRespectsUnits``: ' + QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ + '\n' + '* ``FlagRespectsMapUnitsPerScaleBarUnit``: ' + QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ + '\n' + '* ``FlagUsesUnitLabel``: ' + QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ + '\n' + '* ``FlagUsesSegments``: ' + QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ + '\n' + '* ``FlagUsesLabelBarSpace``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ + '\n' + '* ``FlagUsesLabelVerticalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ + '\n' + '* ``FlagUsesLabelHorizontalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ + '\n' + '* ``FlagUsesAlignment``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ + '\n' + '* ``FlagUsesSubdivisions``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ + '\n' + '* ``FlagUsesDivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionsHeight``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__
# --
# The following has been generated automatically from src/core/qgssnappingconfig.h
QgsSnappingConfig.SnappingMode.baseClass = QgsSnappingConfig
QgsSnappingConfig.SnappingTypes.baseClass = QgsSnappingConfig
QgsSnappingConfig.SnappingTypeFlag.baseClass = QgsSnappingConfig
SnappingTypeFlag = QgsSnappingConfig  # dirty hack since SIP seems to introduce the flags in module
QgsSnappingConfig.ScaleDependencyMode.baseClass = QgsSnappingConfig
# The following has been generated automatically from src/core/symbology/qgsstyleentityvisitor.h
# monkey patching scoped based enum
QgsStyleEntityVisitorInterface.NodeType.Project.__doc__ = "QGIS Project node"
QgsStyleEntityVisitorInterface.NodeType.Layer.__doc__ = "Map layer"
QgsStyleEntityVisitorInterface.NodeType.SymbolRule.__doc__ = "Rule based symbology or label child rule"
QgsStyleEntityVisitorInterface.NodeType.Layouts.__doc__ = "Layout collection"
QgsStyleEntityVisitorInterface.NodeType.PrintLayout.__doc__ = "An individual print layout"
QgsStyleEntityVisitorInterface.NodeType.LayoutItem.__doc__ = "Individual item in a print layout"
QgsStyleEntityVisitorInterface.NodeType.Report.__doc__ = "A QGIS print report"
QgsStyleEntityVisitorInterface.NodeType.ReportHeader.__doc__ = "Report header section"
QgsStyleEntityVisitorInterface.NodeType.ReportFooter.__doc__ = "Report footer section"
QgsStyleEntityVisitorInterface.NodeType.ReportSection.__doc__ = "Report sub section"
QgsStyleEntityVisitorInterface.NodeType.Annotations.__doc__ = "Annotations collection"
QgsStyleEntityVisitorInterface.NodeType.Annotation.__doc__ = "An individual annotation"
QgsStyleEntityVisitorInterface.NodeType.__doc__ = 'Describes the types of nodes which may be visited by the visitor.\n\n' + '* ``Project``: ' + QgsStyleEntityVisitorInterface.NodeType.Project.__doc__ + '\n' + '* ``Layer``: ' + QgsStyleEntityVisitorInterface.NodeType.Layer.__doc__ + '\n' + '* ``SymbolRule``: ' + QgsStyleEntityVisitorInterface.NodeType.SymbolRule.__doc__ + '\n' + '* ``Layouts``: ' + QgsStyleEntityVisitorInterface.NodeType.Layouts.__doc__ + '\n' + '* ``PrintLayout``: ' + QgsStyleEntityVisitorInterface.NodeType.PrintLayout.__doc__ + '\n' + '* ``LayoutItem``: ' + QgsStyleEntityVisitorInterface.NodeType.LayoutItem.__doc__ + '\n' + '* ``Report``: ' + QgsStyleEntityVisitorInterface.NodeType.Report.__doc__ + '\n' + '* ``ReportHeader``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportHeader.__doc__ + '\n' + '* ``ReportFooter``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportFooter.__doc__ + '\n' + '* ``ReportSection``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportSection.__doc__ + '\n' + '* ``Annotations``: ' + QgsStyleEntityVisitorInterface.NodeType.Annotations.__doc__ + '\n' + '* ``Annotation``: ' + QgsStyleEntityVisitorInterface.NodeType.Annotation.__doc__
# --
# The following has been generated automatically from src/core/qgstaskmanager.h
QgsTask.TaskStatus.baseClass = QgsTask
# The following has been generated automatically from src/core/textrenderer/qgstextcharacterformat.h
# monkey patching scoped based enum
QgsTextCharacterFormat.BooleanValue.NotSet.__doc__ = "Property is not set"
QgsTextCharacterFormat.BooleanValue.SetTrue.__doc__ = "Property is set and ``True``"
QgsTextCharacterFormat.BooleanValue.SetFalse.__doc__ = "Property is set and ``False``"
QgsTextCharacterFormat.BooleanValue.__doc__ = 'Status values for boolean format properties\n\n' + '* ``NotSet``: ' + QgsTextCharacterFormat.BooleanValue.NotSet.__doc__ + '\n' + '* ``SetTrue``: ' + QgsTextCharacterFormat.BooleanValue.SetTrue.__doc__ + '\n' + '* ``SetFalse``: ' + QgsTextCharacterFormat.BooleanValue.SetFalse.__doc__
# --
# The following has been generated automatically from src/core/qgstolerance.h
QgsTolerance.UnitType.baseClass = QgsTolerance
# The following has been generated automatically from src/core/qgsunittypes.h
QgsUnitTypes.SystemOfMeasurement.baseClass = QgsUnitTypes
QgsUnitTypes.DistanceUnit.baseClass = QgsUnitTypes
QgsUnitTypes.AreaUnit.baseClass = QgsUnitTypes
QgsUnitTypes.VolumeUnit.baseClass = QgsUnitTypes
QgsUnitTypes.AngleUnit.baseClass = QgsUnitTypes
QgsUnitTypes.TemporalUnit.baseClass = QgsUnitTypes
QgsUnitTypes.RenderUnit.baseClass = QgsUnitTypes
QgsUnitTypes.LayoutUnit.baseClass = QgsUnitTypes
# The following has been generated automatically from src/core/qgsvectorlayer.h
QgsVectorLayer.EditResult.baseClass = QgsVectorLayer
QgsVectorLayer.SelectBehavior.baseClass = QgsVectorLayer
# The following has been generated automatically from src/core/qgsvectorlayerserverproperties.h
QgsVectorLayerServerProperties.PredefinedWmsDimensionName.baseClass = QgsVectorLayerServerProperties
# The following has been generated automatically from src/core/qgsvectorsimplifymethod.h
QgsVectorSimplifyMethod.SimplifyHint.baseClass = QgsVectorSimplifyMethod
QgsVectorSimplifyMethod.SimplifyHints.baseClass = QgsVectorSimplifyMethod
SimplifyHints = QgsVectorSimplifyMethod  # dirty hack since SIP seems to introduce the flags in module
QgsVectorSimplifyMethod.SimplifyAlgorithm.baseClass = QgsVectorSimplifyMethod
# The following has been generated automatically from src/core/geometry/qgswkbtypes.h
QgsWkbTypes.Type.baseClass = QgsWkbTypes
QgsWkbTypes.GeometryType.baseClass = QgsWkbTypes
