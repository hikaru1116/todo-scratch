import React from "react";
import Typography from "@mui/material/Typography";

const Typography4 = ({ color, align, children }) => {
  const typoColor = color != null ? color : "#111111";
  const typoAlign = align != null ? align : "left";

  return (
    <Typography align={typoAlign} fontSize={12} sx={{ color: typoColor }}>
      {children}
    </Typography>
  );
};

export default Typography4;
