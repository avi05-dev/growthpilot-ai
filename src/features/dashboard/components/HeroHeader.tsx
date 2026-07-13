import RefreshIcon from '@mui/icons-material/Refresh';
import TravelExploreIcon from '@mui/icons-material/TravelExplore';
import { Box, Button, Chip, Stack, Typography } from '@mui/material';

const dateFormatter = new Intl.DateTimeFormat(undefined, {
  weekday: 'long',
  month: 'long',
  day: 'numeric',
  year: 'numeric',
});

type HeroHeaderProps = {
  onRefresh: () => void;
};

export function HeroHeader({ onRefresh }: HeroHeaderProps) {
  const today = dateFormatter.format(new Date());

  return (
    <Box
      component="section"
      aria-labelledby="workspace-title"
      sx={{
        border: '1px solid',
        borderColor: 'divider',
        borderRadius: 4,
        p: { xs: 3, md: 5 },
        background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.98), rgba(79, 70, 229, 0.88))',
        color: 'primary.contrastText',
        overflow: 'hidden',
        position: 'relative',
      }}
    >
      <Box sx={{ position: 'absolute', inset: 'auto -12% -45% auto', width: 360, height: 360, borderRadius: '50%', bgcolor: 'rgba(255,255,255,0.12)' }} />
      <Stack spacing={3} sx={{ position: 'relative' }}>
        <Stack direction="row" justifyContent="space-between" alignItems="flex-start" gap={2} flexWrap="wrap">
          <Box>
            <Typography variant="overline" sx={{ opacity: 0.78, fontWeight: 900 }}>
              Good Morning 👋
            </Typography>
            <Typography id="workspace-title" variant="h1" sx={{ fontSize: { xs: 38, md: 58 }, maxWidth: 760, mt: 1 }}>
              Today&apos;s AI Growth Briefing
            </Typography>
            <Typography variant="subtitle1" sx={{ color: 'rgba(255,255,255,0.78)', mt: 2, maxWidth: 680 }}>
              Decide what to learn, create, and publish today with one focused workspace for professional growth.
            </Typography>
          </Box>
          <Chip label="Mock Data" sx={{ bgcolor: 'rgba(255,255,255,0.16)', color: 'inherit', border: '1px solid rgba(255,255,255,0.22)' }} />
        </Stack>
        <Stack direction={{ xs: 'column', sm: 'row' }} spacing={1.5} alignItems={{ sm: 'center' }}>
          <Button variant="contained" color="secondary" startIcon={<RefreshIcon />} onClick={onRefresh} aria-label="Refresh briefing mock data">
            Refresh Briefing
          </Button>
          <Button variant="outlined" startIcon={<TravelExploreIcon />} sx={{ color: 'inherit', borderColor: 'rgba(255,255,255,0.34)' }}>
            View Trends
          </Button>
          <Typography variant="body2" sx={{ color: 'rgba(255,255,255,0.72)', ml: { sm: 1 } }}>
            {today}
          </Typography>
        </Stack>
      </Stack>
    </Box>
  );
}
