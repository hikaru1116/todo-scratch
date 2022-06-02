import React from "react";
import Typography from "@mui/material/Typography";

const Typography3 = ({ color, align, fontWeight, children }) => {
  const _typoColor = color != null ? color : "#111111";
  const _typoAlign = align != null ? align : "left";
  const _fontWeight = fontWeight != null ? fontWeight : "regular";

  return (
    <Typography
      align={_typoAlign}
      fontSize={16}
      fontWeight={_fontWeight}
      sx={{ color: _typoColor }}
    >
      {children}
    </Typography>
  );
};

export default Typography3;
