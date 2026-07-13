import { Card, CardContent } from '@mui/material';
import type { CardProps } from '@mui/material/Card';
import type { Theme } from '@mui/material/styles';
import type { SxProps } from '@mui/system';
import type { PropsWithChildren } from 'react';

function mergeSx(sx: CardProps['sx']): SxProps<Theme> {
  return Array.isArray(sx) ? [{ height: '100%' }, ...sx] : [{ height: '100%' }, sx];
}

export function DashboardCard({ children, sx, ...props }: PropsWithChildren<CardProps>) {
  return (
    <Card sx={mergeSx(sx)} {...props}>
      <CardContent sx={{ p: { xs: 2.5, md: 3 }, '&:last-child': { pb: { xs: 2.5, md: 3 } } }}>{children}</CardContent>
    </Card>
  );
}
