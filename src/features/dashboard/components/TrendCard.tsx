import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import { Box, Button, Chip, LinearProgress, Stack, Typography } from '@mui/material';

import type { Trend } from '../types/dashboard';
import { DashboardCard } from './DashboardCard';

type TrendCardProps = {
  trend: Trend;
};

export function TrendCard({ trend }: TrendCardProps) {
  return (
    <DashboardCard>
      <Stack spacing={2.25}>
        <Stack direction="row" justifyContent="space-between" alignItems="flex-start" gap={2}>
          <Box>
            <Typography variant="h6" component="h3">
              {trend.title}
            </Typography>
            <Typography variant="body2" color="text.secondary" sx={{ mt: 0.75 }}>
              {trend.description}
            </Typography>
          </Box>
          <Chip label={trend.category} color="secondary" size="small" />
        </Stack>

        <Box>
          <Stack direction="row" justifyContent="space-between" sx={{ mb: 0.75 }}>
            <Typography variant="caption" color="text.secondary" fontWeight={800}>
              Trend score
            </Typography>
            <Typography variant="caption" fontWeight={900}>
              {trend.score}/100
            </Typography>
          </Stack>
          <LinearProgress variant="determinate" value={trend.score} aria-label={`${trend.title} trend score`} sx={{ height: 8, borderRadius: 999 }} />
        </Box>

        <Stack direction="row" flexWrap="wrap" gap={1} aria-label={`${trend.title} mock sources`}>
          {trend.sources.map((source) => (
            <Chip key={source} label={source} variant="outlined" size="small" />
          ))}
        </Stack>

        <Button variant="outlined" startIcon={<AutoAwesomeIcon />} aria-label={`Generate content for ${trend.title}`}>
          Generate Content
        </Button>
      </Stack>
    </DashboardCard>
  );
}
