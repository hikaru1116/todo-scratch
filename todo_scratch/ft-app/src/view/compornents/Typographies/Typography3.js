import React from "react";
import Typography from "@mui/material/Typography";

const Typography3 = ({ color, align, fontWeight, children, lineHeight }) => {
  const _typoColor = color != null ? color : "#111111";
  const _typoAlign = align != null ? align : "left";
  const _fontWeight = fontWeight != null ? fontWeight : "regular";
  const _lineHeight = lineHeight != null ? lineHeight : "nomal";

  return (
    <Typography
      align={_typoAlign}
      fontSize={16}
      fontWeight={_fontWeight}
      lineHeight={_lineHeight}
      sx={{ color: _typoColor }}
    >
      {children}
    </Typography>
  );
};

export default Typography3;
