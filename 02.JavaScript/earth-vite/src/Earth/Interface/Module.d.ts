declare interface Module {
  //账户设置
  AccountPresenter_AddDelegate(): any;

  AccountPresenter_CompleteSignIn(): any;

  AccountPresenter_CompleteSignInWithAuthToken(): any;

  AccountPresenter_ForceSignOut(): any;

  AccountPresenter_RefreshUserAccount(): any;

  AccountPresenter_RemoveDelegate(): any;

  AccountPresenter_RequestSignIn(): any;

  AccountPresenter_SetAuthToken(): any;

  AccountPresenter_SignOut(): any;

  //应用信息
  AppInfoPresenter_AddDelegate(): any;

  AppInfoPresenter_GetCopyrightUrl(): any;

  AppInfoPresenter_GetPickerServiceUrl(): any;

  AppInfoPresenter_GetPrivacyPolicyUrl(): any;

  AppInfoPresenter_GetSupportUrl(): any;

  AppInfoPresenter_GetTermsOfServiceUrl(): any;

  AppInfoPresenter_RemoveDelegate(): any;

  AppInfoPresenter_SetLegalDocsLanguageCode(): any;

  AppThemePresenter_AddDelegate(): any;

  AppThemePresenter_RemoveDelegate(): any;

  BalloonPresenter_AddDelegate(): any;

  BalloonPresenter_EditFeature(): any;

  BalloonPresenter_ExitPlayMode(): any;

  BalloonPresenter_HandleKmlLink(): any;

  BalloonPresenter_HideBalloon(): any;

  BalloonPresenter_HidePanel(): any;

  BalloonPresenter_LogNonKmlEarthFeedLink(): any;

  BalloonPresenter_RecenterCurrentFeature(): any;

  BalloonPresenter_RecenterCurrentPlayModeFeature(): any;

  BalloonPresenter_RemoveDelegate(): any;

  BalloonPresenter_RequestLayerOpacityUpdate(): any;

  BalloonPresenter_RequestLocalResourceBytes(): any;

  BalloonPresenter_RestartPlayMode(): any;

  BalloonPresenter_SetLayerOpacity(): any;

  BalloonPresenter_ShowMediaInLightbox(): any;

  BalloonPresenter_VideoPause(): any;

  BalloonPresenter_VideoPlay(): any;

  BalloonPresenter_VideoSetFrame(): any;

  //地球图层设置
  BaseLayerPresenter_AddDelegate(): any;

  BaseLayerPresenter_GetLocale(): any;

  BaseLayerPresenter_HideMapStyles(): any;

  BaseLayerPresenter_ProvideLocalizedMessages(): any;

  BaseLayerPresenter_RefreshBaseLayerStyles(): any;

  BaseLayerPresenter_RefreshCloudAnimationEnabled(): any;

  BaseLayerPresenter_RefreshGridlinesEnabled(): any;

  BaseLayerPresenter_RefreshLayerVisibilities(): any;

  BaseLayerPresenter_RefreshLayers(): any;

  BaseLayerPresenter_RemoveDelegate(): any;

  BaseLayerPresenter_SetBaseLayerStyle(style: number): any;

  BaseLayerPresenter_SetCloudAnimationEnabled(): any;

  BaseLayerPresenter_SetFeatureCategoryVisibility(): any;

  BaseLayerPresenter_SetGridlinesStyle(): any;

  BaseLayerPresenter_SetThreeDImageryEnabled(): any;

  BaseLayerPresenter_SetVisibility(): any;

  BaseLayerPresenter_ShowMapStyles(): any;

  BaseLayerPresenter_ToggleMapStyles(): any;

  BindingError(): any;

  //知识卡片设置
  CardPresenter_AddDelegate(): any;

  CardPresenter_CollapseKnowledgeCard(): any;

  CardPresenter_ExpandKnowledgeCard(): any;

  CardPresenter_FlyToKnowledgeCard(): any;

  CardPresenter_GetStaticMapsUrl(): any;

  CardPresenter_HandleCardActionSelection(): any;

  CardPresenter_HideKnowledgeCard(): any;

  CardPresenter_NormalizeKnowledgeCard(): any;

  CardPresenter_RefreshAddToMyPlacesButtonEnabled(): any;

  CardPresenter_RemoveDelegate(): any;

  CardPresenter_SaveToNewLocalProject(): any;

  CardPresenter_SaveToNewProject(): any;

  CardPresenter_SaveToProject(): any;

  CardPresenter_SaveToProjects(): any;

  CardPresenter_SetCurrentCardIndex(): any;

  CardPresenter_SetStaticMapImageSizes(): any;

  CardPresenter_ShowInfoForKnowledgeGraphMachineId(): any;

  CelestialPresenter_AddDelegate(): any;

  CelestialPresenter_GetCelestialDateTime(): any;

  CelestialPresenter_GetCelestialEnabled(): any;

  CelestialPresenter_GetCurrentCelestialBody(): any;

  CelestialPresenter_RemoveDelegate(): any;

  CelestialPresenter_SetCelestialDateTime(): any;

  CelestialPresenter_SetCelestialEnabled(): any;

  CelestialPresenter_SetCurrentCelestialBody(): any;

  //罗盘设置
  CompassPresenter_AddDelegate(): any;

  CompassPresenter_RemoveDelegate(): any;

  CompassPresenter_ResetAll(): any;

  CompassPresenter_ResetHeading(): any;

  CompassPresenter_ResetTilt(): any;

  CompassPresenter_SetHeading(a: number, b: any): any;

  CompassPresenter_SetTilt(a: number, b: any): any;

  ConfigPresenter_AddDelegate(): any;

  ConfigPresenter_RemoveDelegate(): any;

  ConfigPresenter_RetryConfigRequest(): any;

  //CSV导入设置
  CsvImportPresenter_AddDelegate(): any;

  CsvImportPresenter_ClosePanel(): any;

  CsvImportPresenter_FetchTableContent(): any;

  CsvImportPresenter_Recenter(): any;

  CsvImportPresenter_RemoveDelegate(): any;

  CsvImportPresenter_RequestColumnTypes(): any;

  CsvImportPresenter_SetColumnType(): any;

  CsvImportPresenter_SetFileContent(): any;

  CsvImportPresenter_SetFileLoadingError(): any;

  DocumentPickerPresenter_AddDelegate(): any;

  DocumentPickerPresenter_DialogCancelled(): any;

  DocumentPickerPresenter_DialogConfirmed(): any;

  DocumentPickerPresenter_RemoveDelegate(): any;

  //文档分享设置
  DocumentSharingPresenter_AddDelegate(): any;

  DocumentSharingPresenter_CancelShare(): any;

  DocumentSharingPresenter_ConfirmShare(): any;

  DocumentSharingPresenter_RemoveDelegate(): any;

  //文档视图设置
  DocumentViewPresenter_AddDelegate(): any;

  DocumentViewPresenter_AdjustOpacity(): any;

  DocumentViewPresenter_CancelCopyDocument(): any;

  DocumentViewPresenter_ConfirmCopyDocument(): any;

  DocumentViewPresenter_Delete(): any;

  DocumentViewPresenter_DeleteDocument(): any;

  DocumentViewPresenter_DeleteSelectedFeatures(): any;

  DocumentViewPresenter_EditProperties(): any;

  DocumentViewPresenter_ExportAsKml(): any;

  DocumentViewPresenter_ExportAsKmlWithExtensions(): any;

  DocumentViewPresenter_FlyTo(): any;

  DocumentViewPresenter_GoBack(): any;

  DocumentViewPresenter_HideDocumentView(): any;

  DocumentViewPresenter_HideDocumentViewStack(): any;

  DocumentViewPresenter_Highlight(): any;

  DocumentViewPresenter_ImportToCloud(): any;

  DocumentViewPresenter_MoveSelectedFeatures(): any;

  DocumentViewPresenter_PerformUndo(): any;

  DocumentViewPresenter_PrepareForDragOperation(): any;

  DocumentViewPresenter_QuickShareDocument(): any;

  DocumentViewPresenter_RefreshTiledLayersExperimentEnabled(): any;

  DocumentViewPresenter_ReloadDocument(): any;

  DocumentViewPresenter_RemoveDelegate(): any;

  DocumentViewPresenter_ReportAbuse(): any;

  DocumentViewPresenter_RequestCopyDocument(): any;

  DocumentViewPresenter_SetDocumentDescription(): any;

  DocumentViewPresenter_SetDocumentTitle(): any;

  DocumentViewPresenter_SetFeatureName(): any;

  DocumentViewPresenter_SetOpacity(): any;

  DocumentViewPresenter_SetSelection(): any;

  DocumentViewPresenter_ShareDocument(): any;

  DocumentViewPresenter_ShowBalloon(): any;

  DocumentViewPresenter_ShowBalloonAndFlyTo(): any;

  DocumentViewPresenter_ShowDocumentViewStack(): any;

  DocumentViewPresenter_StartPlayMode(): any;

  DocumentViewPresenter_StartPlayModeAtFeature(): any;

  DocumentViewPresenter_ToggleOpened(): any;

  DocumentViewPresenter_ToggleVisibility(): any;

  DocumentViewPresenter_Unhighlight(): any;

  DrawerPresenter_AddDelegate(): any;

  DrawerPresenter_RemoveDelegate(): any;

  //绘图工具设置
  DrawingToolPresenter_AddDelegate(): any;

  DrawingToolPresenter_CancelFeatureCreation(): any;

  DrawingToolPresenter_ConfirmFeatureCreation(): any;

  DrawingToolPresenter_EnterDrawingToolInMode(): any;

  DrawingToolPresenter_ExitDrawingTool(): any;

  DrawingToolPresenter_GetSelectedFeatureKeyAsString(): any;

  DrawingToolPresenter_RemoveDelegate(): any;

  DrawingToolPresenter_RemoveStrokeFromDrawing(): any;

  DrawingToolPresenter_RemoveVertexFromLineString(): any;

  DrawingToolPresenter_SaveToDocument(): any;

  DrawingToolPresenter_SaveToNewDocument(): any;

  DrawingToolPresenter_SaveToNewLocalDocument(): any;

  DrawingToolPresenter_SetAutoSave(): any;

  DrawingToolPresenter_SetCanEditOutsideEditor(): any;

  DrawingToolPresenter_SetClampAltitudeOnDrag(): any;

  DrawingToolPresenter_SetDefaultKmlNames(): any;

  DrawingToolPresenter_StreetViewCapture(): any;

  DrawingToolPresenter_SwitchToBrushMode(): any;

  DrawingToolPresenter_SwitchToLineStringMode(): any;

  DrawingToolPresenter_SwitchToPointMode(): any;

  DrawingToolPresenter_SwitchToSelectionMode(): any;

  //核心
  EarthCore_AddDelegate(): any;

  EarthCore_DoAppExecutedJobs(): any;

  EarthCore_EnqueueTouch(): any;

  EarthCore_Init(): any;

  EarthCore_IonRemoteGet(): any;

  EarthCore_IsSceneSteady(): any;

  EarthCore_RemoveDelegate(): any;

  EarthCore_SetAuthToken(): any;

  EarthCore_SetFormFactor(): any;

  EarthCore_SetMirthMemoryUsageTargetMb(): any;

  EarthCore_WtfProfileGet(): any;

  ExitStatus(): any;

  ExperimentsPresenter_AddDelegate(): any;

  ExperimentsPresenter_RemoveDelegate(): any;

  ExperimentsPresenter_SetExperimentFlags(): any;

  ExperimentsPresenter_SetPhenotypeServerToken(): any;

  FS_createDataFile(): any;

  FS_createDevice(): any;

  FS_createLazyFile(): any;

  FS_createPath(): any;

  FS_createPreloadedFile(): any;

  FS_unlink(): any;

  //项目设置
  FeatureCreationPresenter_AddDelegate(): any;

  FeatureCreationPresenter_CreateFeature(): any;

  FeatureCreationPresenter_RemoveDelegate(): any;

  FeatureCreationPresenter_SetDefaultFolderName(): any;

  FeatureCreationPresenter_SetDefaultOverlayName(): any;

  FeatureCreationPresenter_SetDefaultSlideName(): any;

  FeaturePreviewCardPresenter_AddDelegate(): any;

  FeaturePreviewCardPresenter_EditFeature(): any;

  FeaturePreviewCardPresenter_HideFeaturePreviewCard(): any;

  FeaturePreviewCardPresenter_RecenterFeature(): any;

  FeaturePreviewCardPresenter_RemoveDelegate(): any;

  //反馈
  FeedbackPresenter_AddDelegate(): any;

  FeedbackPresenter_CaptureCameraData(): any;

  FeedbackPresenter_CaptureEarthView(): any;

  FeedbackPresenter_RemoveDelegate(): any;

  FeelingLuckyPresenter_AddDelegate(): any;

  FeelingLuckyPresenter_RemoveDelegate(): any;

  FeelingLuckyPresenter_ShowInfoForRandomEntity(): any;

  //右下角按键
  HoverButtonPresenter_AddDelegate(): any;

  HoverButtonPresenter_RemoveDelegate(): any;

  HoverButtonPresenter_ShowMapStyles(): any;

  HoverButtonPresenter_TransitionViewTo2D(): any;

  HoverButtonPresenter_TransitionViewTo3D(): any;

  InternalError(): any;

  LightboxPresenter_AddDelegate(): any;

  LightboxPresenter_HideLightbox(): any;

  LightboxPresenter_RemoveDelegate(): any;

  LightboxPresenter_SetMaxImageSize(): any;

  //本地文件
  LocalFileSystemPresenter_AddDelegate(): any;

  LocalFileSystemPresenter_AddFileError(): any;

  LocalFileSystemPresenter_AddFileSuccess(): any;

  LocalFileSystemPresenter_InitAgentError(): any;

  LocalFileSystemPresenter_InitAgentSuccess(): any;

  LocalFileSystemPresenter_ListFilesError(): any;

  LocalFileSystemPresenter_ListFilesSuccess(): any;

  LocalFileSystemPresenter_LoadFileMetadataError(): any;

  LocalFileSystemPresenter_LoadFileMetadataSuccess(): any;

  LocalFileSystemPresenter_ModifyFileError(): any;

  LocalFileSystemPresenter_ModifyFileSuccess(): any;

  LocalFileSystemPresenter_PersistentLocalStorageAvailable(): any;

  LocalFileSystemPresenter_ReadFileError(): any;

  LocalFileSystemPresenter_ReadFileSuccess(): any;

  LocalFileSystemPresenter_RemoveDelegate(): any;

  LocalFileSystemPresenter_RemoveFileError(): any;

  LocalFileSystemPresenter_RemoveFileSuccess(): any;

  LoggingPresenter_AddDelegate(): any;

  LoggingPresenter_LogDeeplink(): any;

  LoggingPresenter_RemoveDelegate(): any;

  //测量工具
  MeasureToolPresenter_AddCenterAndCloseShape(): any;

  MeasureToolPresenter_AddCenterToLineString(): any;

  MeasureToolPresenter_AddDelegate(): any;

  MeasureToolPresenter_AddMeasurementToProject(): any;

  MeasureToolPresenter_AddPoint(): any;

  MeasureToolPresenter_ConfirmMeasurement(): any;

  MeasureToolPresenter_FlyToTopDownView(): any;

  MeasureToolPresenter_RemoveDelegate(): any;

  MeasureToolPresenter_RemoveLastPoint(): any;

  MeasureToolPresenter_RestartMeasurement(): any;

  MeasureToolPresenter_SetAreaUnit(): any;

  MeasureToolPresenter_SetDistanceUnit(): any;

  MeasureToolPresenter_SetLocalizedMeasurementName(): any;

  MeasureToolPresenter_ToggleMeasuring(): any;

  //菜单面板
  MenuPanelPresenter_AddDelegate(): any;

  MenuPanelPresenter_GetLocale(): any;

  MenuPanelPresenter_HideMenuPanel(): any;

  MenuPanelPresenter_RemoveDelegate(): any;

  MenuPanelPresenter_ShowMapStyles(): any;

  MenuPanelPresenter_ShowMyPlaces(): any;

  MenuPanelPresenter_ShowSearch(): any;

  MenuPanelPresenter_ShowSettings(): any;

  MenuPanelPresenter_ShowVoyager(): any;

  //我的位置
  MyLocationPresenter_AddDelegate(): any;

  MyLocationPresenter_DisableOverlay(): any;

  MyLocationPresenter_EnableCameraTracking(): any;

  MyLocationPresenter_EnableLocationPermissions(): any;

  MyLocationPresenter_EnableOverlay(): any;

  MyLocationPresenter_Recenter(): any;

  MyLocationPresenter_RemoveDelegate(): any;

  MyLocationPresenter_Update(): any;

  //我的地点
  MyPlacesPresenter_AddDelegate(): any;

  MyPlacesPresenter_AddDocumentWithKmlContent(): any;

  MyPlacesPresenter_AddDocumentWithUmsMapId(): any;

  MyPlacesPresenter_AddDocumentWithUrl(): any;

  MyPlacesPresenter_AddEmptyLocalDocument(): any;

  MyPlacesPresenter_AddEmptyUmsDocument(): any;

  MyPlacesPresenter_ClearRecentList(): any;

  MyPlacesPresenter_DeleteDocument(): any;

  MyPlacesPresenter_ExportAsKml(): any;

  MyPlacesPresenter_FlyToDocument(): any;

  MyPlacesPresenter_GetOnePickV2ServiceUrl(): any;

  MyPlacesPresenter_GetPickerServiceUrl(): any;

  MyPlacesPresenter_HideMyPlaces(): any;

  MyPlacesPresenter_OpenKmlFromUri(kml_file: string): any;

  MyPlacesPresenter_ReadKmlFileContentFailed(): any;

  MyPlacesPresenter_RemoveDelegate(): any;

  MyPlacesPresenter_RemoveDocumentFromRecent(): any;

  MyPlacesPresenter_RequestCsvImportFromGoogleDrive(): any;

  MyPlacesPresenter_RequestCsvImportFromLocalDisk(): any;

  MyPlacesPresenter_SetDefaultDocumentName(): any;

  MyPlacesPresenter_SetDescription(): any;

  MyPlacesPresenter_SetFocusedDocumentKey(): any;

  MyPlacesPresenter_SetPinned(): any;

  MyPlacesPresenter_SetRecoveringDocumentName(): any;

  MyPlacesPresenter_SetTitle(): any;

  MyPlacesPresenter_SetUntitledDocumentName(): any;

  MyPlacesPresenter_SetVisibility(): any;

  MyPlacesPresenter_ShowMyPlaces(): any;

  MyPlacesPresenter_SortKmlDocuments(): any;

  MyPlacesPresenter_SortPinnedDocuments(): any;

  MyPlacesPresenter_StartPlayMode(): any;

  MyPlacesPresenter_ToggleMyPlaces(): any;

  MyPlacesPresenter_TogglePinned(): any;

  MyPlacesPresenter_ToggleVisibility(): any;

  //导航球
  NavGlobePresenter_AddDelegate(): any;

  NavGlobePresenter_FlyToLatLng(
    latitude: number,
    longitude: number,
    altitude: number
  ): any;

  NavGlobePresenter_RefreshViewParams(): any;

  NavGlobePresenter_RemoveDelegate(): any;

  NavGlobePresenter_ResetToSpaceView(): any;

  NavGlobePresenter_StopCameraMotion(): any;

  //网络
  NetworkMonitorPresenter_AddDelegate(): any;

  NetworkMonitorPresenter_DismissToast(): any;

  NetworkMonitorPresenter_RemoveDelegate(): any;

  //演示模式
  PlayModePresenter_AddDelegate(): any;

  PlayModePresenter_HideTableOfContents(): any;

  PlayModePresenter_RecenterCurrentFeature(): any;

  PlayModePresenter_RemoveDelegate(): any;

  PlayModePresenter_Restart(): any;

  PlayModePresenter_ShareStory(): any;

  PlayModePresenter_ShowFeatureAtIndex(): any;

  PlayModePresenter_ShowNextFeature(): any;

  PlayModePresenter_ShowPreviousFeature(): any;

  PlayModePresenter_ShowTableOfContents(): any;

  PlayModePresenter_Stop(): any;

  PropertyEditorPresenter_AddDelegate(): any;

  PropertyEditorPresenter_CloseEditor(): any;

  PropertyEditorPresenter_DeleteFeatureAndCloseEditor(): any;

  PropertyEditorPresenter_HideCreateLinkDialog(): any;

  PropertyEditorPresenter_InsertWidget(): any;

  PropertyEditorPresenter_OpenEditor(): any;

  PropertyEditorPresenter_PreloadIcons(): any;

  PropertyEditorPresenter_RemoveDelegate(): any;

  PropertyEditorPresenter_SetMaxThumbnailImageSize(): any;

  PropertyEditorPresenter_ShowCreateLinkDialog(): any;

  PropertyEditorPresenter_ShowInfo(): any;

  PropertyEditorPresenter_SnapshotView(): any;

  PropertyEditorPresenter_SwitchToHtmlMode(): any;

  PropertyEditorPresenter_SwitchToTemplateMode(): any;

  PropertyEditorPresenter_Update(): any;

  //快速分享
  QuickSharingPresenter_AddDelegate(): any;

  QuickSharingPresenter_CloseDialog(): any;

  QuickSharingPresenter_RemoveDelegate(): any;

  QuickSharingPresenter_ShareLink(): any;

  QuickSharingPresenter_ToggleSharing(): any;

  //搜索
  SearchPresenter_AddDelegate(): any;

  SearchPresenter_CancelCurrentSearch(): any;

  SearchPresenter_ClearKmlSearchFolder(): any;

  SearchPresenter_ClearSearchHistory(): any;

  SearchPresenter_FlyToResult(): any;

  SearchPresenter_HideSearchHistory(): any;

  SearchPresenter_HideSearchPanel(): any;

  SearchPresenter_PerformGroupCommand(): any;

  SearchPresenter_PerformResultCommand(): any;

  SearchPresenter_ProvideLocalizedMessages(): any;

  SearchPresenter_RemoveDelegate(): any;

  SearchPresenter_RequestSearchResultGroupPage(): any;

  SearchPresenter_SearchForNextPage(): any;

  SearchPresenter_SearchForPrevPage(): any;

  SearchPresenter_SetEarthViewVisibleHeightPercentageDuringSearch(): any;

  SearchPresenter_SetSearchState(): any;

  SearchPresenter_SetShouldPerformSingleResultCommand(): any;

  SearchPresenter_ShowInfoForFeature(): any;

  SearchPresenter_ShowSearchPanel(): any;

  SearchPresenter_StartGetSearchSuggestions(): any;

  SearchPresenter_ToggleSearchPanel(): any;

  SetRenderedString(): any;

  //设置界面
  SettingsPresenter_AddDelegate(): any;

  SettingsPresenter_BackfillDefaultEntries(): any;

  SettingsPresenter_ClearCache(): any;

  SettingsPresenter_ClearSearchHistory(): any;

  SettingsPresenter_ClearValue(): any;

  SettingsPresenter_GetValue(): any;

  SettingsPresenter_HideSettings(): any;

  SettingsPresenter_Init(): any;

  SettingsPresenter_RemoveDelegate(): any;

  SettingsPresenter_Reset(): any;

  SettingsPresenter_ResetSettingsToDefault(): any;

  SettingsPresenter_SetMirthClickMaxDelay(): any;

  SettingsPresenter_SetValue(key: string, value: string): any;

  SettingsPresenter_ShowSettings(): any;

  SettingsPresenter_Sync(): any;

  SharingPolicyPresenter_AddDelegate(): any;

  SharingPolicyPresenter_RemoveDelegate(): any;

  SharingPolicyPresenter_SharingPolicyAccepted(): any;

  SharingPolicyPresenter_SharingPolicyRejected(): any;

  SixAxisInputPresenter_AddDelegate(): any;

  SixAxisInputPresenter_NotifyDisconnected(): any;

  SixAxisInputPresenter_RemoveDelegate(): any;

  SixAxisInputPresenter_SetAxisValues(): any;

  //喷漆？？
  SprayPaintPresenter_AddDelegate(): any;

  SprayPaintPresenter_ClosePanel(): any;

  SprayPaintPresenter_PerformRedo(): any;

  SprayPaintPresenter_PerformUndo(): any;

  SprayPaintPresenter_RemoveDelegate(): any;

  SprayPaintPresenter_SelectBrushTool(): any;

  SprayPaintPresenter_SelectEraserTool(): any;

  SprayPaintPresenter_SelectMoveTool(): any;

  SprayPaintPresenter_SetBorderColor(): any;

  SprayPaintPresenter_SetBorderThickness(): any;

  SprayPaintPresenter_SetBrushOpacity(): any;

  SprayPaintPresenter_SetBrushSize(): any;

  SprayPaintPresenter_SetFillColor(): any;

  SprayPaintPresenter_SetLocalizedText(): any;

  //URL
  StateUrlPresenter_AddDelegate(): any;

  StateUrlPresenter_CreateFirebaseDynamicLink(): any;

  StateUrlPresenter_GetCurrentCameraStateUrl(): any;

  StateUrlPresenter_GetCurrentPath(): any;

  StateUrlPresenter_GetCurrentStateUrl(): any;

  StateUrlPresenter_GetCurrentVoyagerStoryUrl(): any;

  StateUrlPresenter_ParseStateFromPath(): any;

  StateUrlPresenter_ParseStateFromUrl(): any;

  StateUrlPresenter_RemoveDelegate(): any;

  StateUrlPresenter_RequestFirebaseDynamicLink(): any;

  //街景
  StreetViewPresenter_AddDelegate(): any;

  StreetViewPresenter_EndPanView(): any;

  StreetViewPresenter_EnterStreetView(): any;

  StreetViewPresenter_KeyboardEnterStreetView(lat: number, lon: number): any;

  StreetViewPresenter_LeaveStreetView(): any;

  StreetViewPresenter_RemoveDelegate(): any;

  StreetViewPresenter_SetCoverageOverlayVisible(visible: number): any;

  StreetViewPresenter_StartPanView(): any;

  StreetViewPresenter_UpdatePanViewSpeed(): any;

  //系统
  SystemPresenter_AddDelegate(): any;

  SystemPresenter_RemoveDelegate(): any;

  SystemPresenter_SetMemoryUsageTargetMb(MemoryMb: number): any;

  SystemPresenter_SetRenderSceneEnabled(): any;

  //时光机器
  TimeMachinePresenter_Activate(): any;

  TimeMachinePresenter_AddDelegate(): any;

  TimeMachinePresenter_Collapse(): any;

  TimeMachinePresenter_Deactivate(): any;

  TimeMachinePresenter_Expand(): any;

  TimeMachinePresenter_MoveCameraToRecommendedTimelapseAltitude(): any;

  TimeMachinePresenter_PauseTimelapse(): any;

  TimeMachinePresenter_RemoveDelegate(): any;

  TimeMachinePresenter_RequestShowHelp(): any;

  TimeMachinePresenter_SeekNext(): any;

  TimeMachinePresenter_SeekPrevious(): any;

  TimeMachinePresenter_SetDate(): any;

  TimeMachinePresenter_SetTimelapseFramerateMultiplier(): any;

  TimeMachinePresenter_StartTimelapse(): any;

  TimeMachinePresenter_StopTimelapse(): any;

  TimeMachinePresenter_ToggleLockOnMostRecentDate(): any;

  ToolbarPresenter_AddDelegate(): any;

  ToolbarPresenter_RemoveDelegate(): any;

  ToolbarPresenter_ShowInfoForRandomEntity(): any;

  ToolbarPresenter_ShowVoyager(): any;

  ToolbarPresenter_SwitchToNextCelestialBody(): any;

  ToolbarPresenter_ToggleCelestialTime(): any;

  ToolbarPresenter_ToggleMapStyle(): any;

  ToolbarPresenter_ToggleMeasureTool(): any;

  ToolbarPresenter_ToggleMenuPanel(): any;

  ToolbarPresenter_ToggleMyPlaces(): any;

  ToolbarPresenter_ToggleSearch(): any;

  ToolbarPresenter_ToggleTimeMachine(): any;

  TopLevelViewPresenter_AddDelegate(): any;

  TopLevelViewPresenter_RecalculateTopLevelViewVisibilities(): any;

  TopLevelViewPresenter_RemoveDelegate(): any;

  TopLevelViewPresenter_ToggleFullscreen(): any;

  TopToolbarPresenter_AddDelegate(): any;

  TopToolbarPresenter_RemoveDelegate(): any;

  TopToolbarPresenter_UserActionTriggered(): any;

  TourPresenter_AddDelegate(): any;

  TourPresenter_DismissTour(): any;

  TourPresenter_GetCurrentTime(): any;

  TourPresenter_GetTourDuration(): any;

  TourPresenter_PauseTour(): any;

  TourPresenter_PlayTour(): any;

  TourPresenter_RemoveDelegate(): any;

  TourPresenter_RestartTour(): any;

  TourPresenter_Seek(): any;

  UnboundTypeError(): any;

  UrlSharingPresenter_AddDelegate(): any;

  UrlSharingPresenter_CancelDialog(): any;

  UrlSharingPresenter_ConfirmDialog(): any;

  UrlSharingPresenter_RemoveDelegate(): any;

  UrlSharingPresenter_RequestPostcardImage(): any;

  UrlSharingPresenter_SetAdditionalUrlParameters(): any;

  UrlSharingPresenter_SetApiKey(): any;

  UserErrorsPresenter_AddDelegate(): any;

  UserErrorsPresenter_RemoveDelegate(): any;

  UserErrorsPresenter_TakeAction(): any;

  ViewStatusPresenter_AddDelegate(): any;

  ViewStatusPresenter_RemoveDelegate(): any;

  ViewStatusPresenter_SetMaxScaleBarUiLength(): any;

  ViewStatusPresenter_SetTimeMachineActive(): any;

  VoyagerPresenter_ActivateFeedItem(): any;

  VoyagerPresenter_AddDelegate(): any;

  VoyagerPresenter_DismissFeedItem(): any;

  VoyagerPresenter_ExitVoyagerItem(): any;

  VoyagerPresenter_HideVoyagerGrid(): any;

  VoyagerPresenter_RemoveDelegate(): any;

  VoyagerPresenter_RequestVoyagerContent(): any;

  VoyagerPresenter_RestartFeedItem(): any;

  VoyagerPresenter_SetFeedSuffix(): any;

  VoyagerPresenter_ShowVoyagerGrid(): any;

  VoyagerPresenter_ToggleVoyagerGrid(): any;

  ZoomButtonsPresenter_AddDelegate(): any;

  ZoomButtonsPresenter_RemoveDelegate(): any;

  ZoomButtonsPresenter_StartZoomIn(): any;

  ZoomButtonsPresenter_StartZoomOut(): any;

  ZoomButtonsPresenter_StopZoomIn(): any;

  ZoomButtonsPresenter_StopZoomOut(): any;
}
