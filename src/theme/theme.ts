import { alpha, createTheme } from '@mui/material/styles';

import { designTokens } from './tokens';

export const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: designTokens.colors.brand,
      dark: '#020617',
      light: '#334155',
      contrastText: '#ffffff',
    },
    secondary: {
      main: designTokens.colors.brandAccent,
      dark: '#3730a3',
      light: '#818cf8',
      contrastText: '#ffffff',
    },
    success: {
      main: designTokens.colors.success,
    },
    warning: {
      main: designTokens.colors.warning,
    },
    error: {
      main: designTokens.colors.danger,
    },
    info: {
      main: designTokens.colors.info,
    },
    background: {
      default: '#f6f7fb',
      paper: designTokens.colors.surface,
    },
    text: {
      primary: designTokens.colors.ink,
      secondary: designTokens.colors.inkMuted,
    },
    divider: designTokens.colors.borderSubtle,
  },
  typography: {
    fontFamily: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'].join(','),
    h1: {
      fontWeight: 800,
      letterSpacing: '-0.055em',
      lineHeight: 1.02,
    },
    h4: {
      fontWeight: 800,
      letterSpacing: '-0.04em',
      lineHeight: 1.08,
    },
    h5: {
      fontWeight: 800,
      letterSpacing: '-0.035em',
    },
    h6: {
      fontWeight: 750,
      letterSpacing: '-0.02em',
    },
    subtitle1: {
      lineHeight: 1.7,
    },
    button: {
      fontWeight: 750,
      textTransform: 'none',
    },
  },
  shape: {
    borderRadius: designTokens.radii.md,
  },
  spacing: 8,
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: {
          background:
            'radial-gradient(circle at top left, rgba(79, 70, 229, 0.10), transparent 32rem), linear-gradient(180deg, #fbfcff 0%, #f6f7fb 48%, #f8fafc 100%)',
        },
        'a, button, [role="button"]': {
          '&:focus-visible': {
            outline: 'none',
            boxShadow: designTokens.shadows.focus,
          },
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          border: `1px solid ${designTokens.colors.borderSubtle}`,
          borderRadius: designTokens.radii.lg,
          boxShadow: designTokens.shadows.card,
          backgroundImage: 'none',
        },
      },
    },
    MuiButton: {
      defaultProps: {
        disableElevation: true,
      },
      styleOverrides: {
        root: {
          borderRadius: designTokens.radii.pill,
          paddingInline: 18,
        },
        containedPrimary: {
          background: `linear-gradient(135deg, ${designTokens.colors.brand} 0%, ${alpha(designTokens.colors.brandAccent, 0.92)} 100%)`,
        },
      },
    },
    MuiChip: {
      styleOverrides: {
        root: {
          borderRadius: designTokens.radii.pill,
          fontWeight: 700,
        },
      },
    },
  },
});
