import NXOpen

the_session = NXOpen.Session.GetSession()
parts = the_session.Parts
work_part = parts.Work
listing_window = the_session.ListingWindow

dummy_block = NXOpen.Features.Block.Null

builder = work_part.Features.CreateBlockFeatureBuilder(dummy_block)
builder.Type = NXOpen.Features.BlockFeatureBuilderTypes.OriginAndEdgeLengths
origin_point = NXOpen.Point3d(0.0, 0.0, 0.0)

builder.SetOriginAndLengths(origin_point, "1", "1", "1")

builder.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

builder.Commit()
builder.Destroy()
